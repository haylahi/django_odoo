# author: Liberty
# date: 2019/4/28 17:02

from rest_framework import serializers

from . import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseSchool
        fields = '__all__'
        read_only_fields = ('is_active',)


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseGrade
        fields = '__all__'
        read_only_fields = ('is_active',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseCourse
        fields = '__all__'
        read_only_fields = ('is_active',)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'
        read_only_fields = ('is_active',)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseClass
        fields = '__all__'
        read_only_fields = ('is_active',)

    def create(self, attr):
        head_teacher = attr.get('head_teacher')
        # 一个班级只有一个班主任
        _c = head_teacher.head_teacher_class.all()
        if len(_c) == 1 or len(_c) > 0:
            raise serializers.ValidationError('该老师是班级【{}】的班主任, 一个老师只能担任一个班级的班主任'.format(_c[0]))
        return super().create(attr)


class CourseMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassCourseMap
        fields = '__all__'
        read_only_fields = ('is_active', 'create_time')


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Examination
        fields = '__all__'
        read_only_fields = ('is_active', 'create_time', 'is_create_record')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ScoreRecord
        fields = '__all__'
        read_only_fields = ('is_active', 'create_time')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        read_only_fields = ('is_active',)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'
        read_only_fields = ('is_active',)
