import logging
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from django.db import models

# ---------------------------------------------------------

__logger__ = logging.getLogger(__name__)

CHOICES_SEMESTER = [
    ('1', '第一学期'),
    ('2', '第二学期'),
]

CHOICES_LEVEL = [
    ('A', 'A'),  # 86 < x <= 100
    ('B', 'B'),  # 73 < x <= 86
    ('C', 'C'),  # 60 <= x <= 73
    ('D', 'D'),  # 0 <= x < 60
]

CHOICES_EXAMINATION_TYPE = [
    ('m', '期中'),
    ('e', '期末'),
    ('a', '补考'),
    ('r', '重修考试'),
    ('s', '小测试'),
    ('g', '年级统考'),
    ('o', '其他')
]

MAX_GRADE_POINT = '5.0'


def check_score(score):
    try:
        score = float(score)
    except Exception as e:
        __logger__.error(e)
        return False
    if 0 <= score <= 100:
        return True
    else:
        return False


def rounding_score(score, rounding: str = '0.0'):
    if isinstance(score, Decimal):
        origin_num = score
    else:
        origin_num = Decimal(score)
    ret_num = origin_num.quantize(Decimal(rounding), rounding=ROUND_HALF_UP)
    return str(ret_num)


def get_level(score):
    score = Decimal(score)
    if 86 < score <= 100:
        ret = 'A'
    elif 73 < score <= 86:
        ret = 'B'
    elif 60 <= score <= 73:
        ret = 'C'
    else:
        ret = 'D'
    return ret


def compute_grade_point(score: str):
    _num = int(rounding_score(score, '0'))

    if _num == 100:
        return MAX_GRADE_POINT
    if 90 <= _num <= 99:
        _t = 4 + (_num - 90) / 10
        return str(_t)
    if 80 <= _num <= 89:
        _t = 3 + (_num - 80) / 10
        return str(_t)
    if 70 <= _num <= 79:
        _t = 2 + (_num - 70) / 10
        return str(_t)
    if 60 <= _num <= 69:
        _t = 1 + (_num - 60) / 10
        return str(_t)
    if _num < 60:
        return '0'


def compute_passed(score):
    return Decimal(score) >= 60


def convert_to_100(score: str, full_score: str):
    """获取score"""
    _ret = Decimal(score) / Decimal(full_score) * 100
    return rounding_score(_ret)


def compute_credits(grade_point: str, credit: str):
    _num = Decimal(grade_point) * Decimal(credit)
    return rounding_score(_num)


class BaseSchool(models.Model):
    name = models.CharField('学校名称', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    short_name = models.CharField('简称', max_length=255, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseGrade(models.Model):
    """
    一年级一期
    一年级二期
    二年级一期

    """
    name = models.CharField('年级', max_length=255)
    semester = models.CharField('学期(一, 二)', max_length=255, choices=CHOICES_SEMESTER)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.get_semester_display())

    class Meta:
        unique_together = ('name', 'semester')
        ordering = ['name']


class Material(models.Model):
    """
    教材
    一年级语文 。。。

    """

    grade = models.ForeignKey(BaseGrade, on_delete=models.PROTECT, verbose_name='适用年级')
    # 课程可以看成一个分类
    course_info = models.ForeignKey('BaseCourse', on_delete=models.PROTECT, verbose_name='所属课程')
    name = models.CharField('教材名', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    credits = models.CharField('教材学分', max_length=255)
    full_score_tag = models.CharField('满分', max_length=255, default='100')

    teachers = models.ManyToManyField('Teacher', blank=True, verbose_name='教该课程的老师')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseCourse(models.Model):
    """语文 数学 ......"""
    name = models.CharField('课程', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseClass(models.Model):
    school = models.ForeignKey(BaseSchool, on_delete=models.CASCADE, verbose_name='所在学校', related_name='school_classes')
    name = models.CharField('班级', max_length=255)
    code = models.CharField('代号', max_length=255, default='')

    create_year = models.CharField('创建年', max_length=255)
    # 一个班主任只能有一个班级
    head_teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, verbose_name='班主任', related_name='head_teacher_class')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        ordering = ['name']


class ClassCourseMap(models.Model):
    """
    班级选课程表
    一个班级 多少课程

    """
    grade_info = models.ForeignKey(BaseGrade, on_delete=models.PROTECT, verbose_name='当前年级')

    base_class = models.ForeignKey(BaseClass, on_delete=models.PROTECT, verbose_name='所属班级', related_name='class_courses')
    course = models.ForeignKey(BaseCourse, on_delete=models.PROTECT, verbose_name='所选课程')

    # 过滤教材 -->  grade_info  course
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name='所选教材')
    # 过滤 老师
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, verbose_name='任课老师')

    # 过滤条件
    is_use_now = models.BooleanField(default=True, verbose_name='是否为班级正在上的课程')
    create_time = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}-{}-[{}]'.format(self.base_class.name, self.grade_info.name, self.course.name)

    class Meta:
        unique_together = ('grade_info', 'base_class', 'course')
        ordering = ['-create_time']


class Examination(models.Model):
    """
    考试 什么班级 什么课程才会有考试
    班班级的测试
    全校 全年级 全课程的考试
    ......

    """
    name = models.CharField('考试名称', max_length=255)
    course_map = models.ForeignKey(ClassCourseMap, on_delete=models.PROTECT, verbose_name='课程')
    invigilator = models.ForeignKey(
        'Teacher', on_delete=models.PROTECT,
        verbose_name='监考老师', related_name='invigilator_examination'
    )
    read_teacher = models.ForeignKey(
        'Teacher', on_delete=models.PROTECT, null=True, blank=True,
        verbose_name='阅卷老师', related_name='teacher_read_examination'
    )

    test_type = models.CharField('考试类型', max_length=255, choices=CHOICES_EXAMINATION_TYPE)
    test_date = models.DateField('考试时间', null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    is_create_record = models.BooleanField('创建了考试记录', default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def create_score_record(self):
        """
        创建考试记录为每个学生

        """

        _class = self.course_map.base_class
        # 准备数据
        _students = _class.class_students.all().filter(is_active=True)  # list or None
        _date_now = datetime.now()  # datetime
        _full_mark = self.course_map.material.full_score_tag  # str
        _create_teacher = self.read_teacher  # obj or None

        # 创建任务


class ScoreRecord(models.Model):
    """
    考试成绩记录表
    平均绩点  学分绩点和 / 学分和

    """
    examination = models.ForeignKey(Examination, on_delete=models.PROTECT, verbose_name='考试名称', related_name='examination_records')
    student = models.ForeignKey('Student', on_delete=models.PROTECT, verbose_name='考试学生', related_name='student_test_records')

    full_score_tag = models.CharField('满分', max_length=255, default='100')

    #  67.9
    score = models.CharField('分数', max_length=255, default='')
    score_level = models.CharField('得分等级', max_length=255, default='')
    # 根据分数
    grade_point = models.CharField('获得绩点', max_length=255, default='')
    # 根据 绩点* 教材学分
    credits = models.CharField('本次获得学分绩点', max_length=255, default='')

    is_joined = models.BooleanField('是否参加考试', default=True)
    is_passed = models.BooleanField('是否通过考试', default=True)

    # 默认为自己的任课老师
    create_teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    create_time = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}{}'.format(self.student.name, self.score)

    class Meta:
        ordering = ['-score']


class Student(models.Model):
    base_class = models.ForeignKey(BaseClass, on_delete=models.PROTECT, verbose_name='所在班级', related_name='class_students')
    name = models.CharField('学生名称', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Teacher(models.Model):
    name = models.CharField('老师', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
