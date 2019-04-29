from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from base.utils import generate_front_list
from . import models
from . import serializer


class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = models.BaseSchool.objects.filter(is_active=True)
    serializer_class = serializer.SchoolSerializer


class GradeListCreateView(generics.ListCreateAPIView):
    queryset = models.BaseGrade.objects.filter(is_active=True)
    serializer_class = serializer.GradeSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = models.BaseCourse.objects.filter(is_active=True)
    serializer_class = serializer.CourseSerializer


class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = models.Material.objects.filter(is_active=True)
    serializer_class = serializer.MaterialSerializer


class ClassListCreateView(generics.ListCreateAPIView):
    queryset = models.BaseClass.objects.filter(is_active=True)
    serializer_class = serializer.ClassSerializer


class CourseMapListCreateView(generics.ListCreateAPIView):
    queryset = models.ClassCourseMap.objects.filter(is_active=True)
    serializer_class = serializer.CourseMapSerializer


class ExaminationListCreateView(generics.ListCreateAPIView):
    queryset = models.Examination.objects.filter(is_active=True)
    serializer_class = serializer.ExaminationSerializer


class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = models.ScoreRecord.objects.filter(is_active=True)
    serializer_class = serializer.ScoreSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = models.Student.objects.filter(is_active=True)
    serializer_class = serializer.StudentSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.filter(is_active=True)
    serializer_class = serializer.TeacherSerializer


# -------------------------------------------------------------------

def html_examination(request):
    examination_list = models.Examination.objects.filter(is_active=True)
    field_list = ['id', 'name', 'course_map', 'invigilator', 'read_teacher', 'test_type', 'test_date']
    attr = generate_front_list(examination_list, field_list)
    return render(request, 'school/examination_list.html', {
        'model_object': models.Examination,
        'model_data': attr,
        'model_fields': field_list
    })


def html_score_list(request):
    # TODO 分页 把 field_list --> dict str 分数排序 bug   把配置封装成对象
    records = models.ScoreRecord.objects.filter(is_active=True)
    field_list = ['id', 'examination', 'student', 'full_score_tag', 'real_score',
                  'score', 'score_level', 'grade_point', 'credits', 'is_joined', 'is_passed', 'create_teacher']
    editable_field_list = ['real_score', 'is_joined']
    attr = generate_front_list(records, field_list, editable_field_list)
    return render(request, 'school/examination_list.html', {
        'model_object': models.ScoreRecord,
        'model_data': attr,
        'model_fields': field_list,
        'model_colorful_field': 'score_level'
    })


def real_test(request):
    # examination_list = models.Examination.objects.filter(is_active=True)
    # for o in examination_list:
    #     o.create_score_record()

    """
    records = models.ScoreRecord.objects.filter(is_active=True)
    for r in records:
        _pass = random.randint(1, 100)
        _join_tag = True
        if _pass in [1, 2, 3, 4]:
            _join_tag = False
        _real_num = random.randint(0, 100)

        if _join_tag:
            p = models.compute_grade_point(_real_num)
            attr = {
                'real_score': str(_real_num),
                'score': str(_real_num),
                'score_level': models.get_level(_real_num),
                'grade_point': p,
                'credits': models.compute_credits(p, r.examination.course_map.material.credits),
                'is_joined': True,
                'is_passed': models.compute_passed(_real_num)
            }
            models.ScoreRecord.objects.filter(id=r.id).update(**attr)

        else:
            # 没参加考试
            attr = {
                'real_score': '0',
                'score': '0',
                'score_level': 'D',
                'grade_point': "0.0",
                'credits': '0.0',
                'is_joined': False,
                'is_passed': False,
            }
            models.ScoreRecord.objects.filter(id=r.id).update(**attr)
    """

    # objs = models.Material.objects.get(pk=7)
    # teachers = objs.teachers.filter(is_active=True)
    # print(teachers, type(teachers))

    from django.core import paginator

    data_list = ['吴刚',
                 '王浩',
                 '蒋建',
                 '许成',
                 '胡兵',
                 '何凤英',
                 '徐桂兰',
                 '林成',
                 '王倩',
                 '刘明',
                 '支平',
                 '左鑫',
                 '冯岩',
                 '胡婷婷',
                 '谭秀梅',
                 '毛娟',
                 '周晨',
                 '晏坤',
                 '杨婷婷',
                 '周浩',
                 '常玉梅',
                 '文小红',
                 '杨雷',
                 '何玲',
                 '陆强',
                 '杜芳',
                 '华平',
                 '岳桂芳',
                 '赵兰英',
                 '郭鑫',
                 '李海燕',
                 '商云',
                 '蒋阳',
                 '周慧',
                 '莫刚',
                 '马海燕',
                 '翁成',
                 '安坤',
                 '汪桂芳',
                 '李丽丽',
                 '李欢',
                 '蒙勇',
                 '杨斌',
                 '刘建国',
                 '杨建',
                 '陈桂英',
                 '许兰英',
                 '饶秀珍',
                 '叶莉',
                 '马雷',
                 '你好',
                 '你好啊']

    page_obj = paginator.Paginator(data_list, 5, 4, True)

    print('总共数量', page_obj.count)  # 总共数量
    print('可分为多少页', page_obj.num_pages)  # 可分为多少页
    print('xxxx', page_obj.page_range)
    # has_previous 上一页？ has_next 下一页 ？

    for p in page_obj.page_range:
        page_i = page_obj.page(p)
        print('current page list:  当前是第几页{}'.format(page_i.number), page_i.object_list)

    return HttpResponse('200')
