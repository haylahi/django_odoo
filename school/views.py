import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from base.utils import generate_result_list
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
    return render(request, 'table_component.html', {
        'model_object': models.Examination,
        'model_data': examination_list,
        'model_field_list': field_list
    })


def html_score_list(request):
    # TODO 分页 把 field_list --> dict str 分数排序 bug   把配置封装成对象
    records = models.ScoreRecord.objects.filter(is_active=True)
    field_list = ['id', 'examination', 'student', 'full_score_tag', 'real_score',
                  'score', 'score_level', 'grade_point', 'credits', 'is_joined',
                  'is_passed', 'create_teacher']

    return render(request, 'table_component.html', {
        'model_object': models.ScoreRecord,
        'model_data': records,  # 可能为空
        'model_field_list': field_list,
    })


def real_test(request):
    # page_obj = paginator.Paginator(data_list, 5, 4, True)
    #
    # print('总共数量', page_obj.count)  # 总共数量
    # print('可分为多少页', page_obj.num_pages)  # 可分为多少页
    # print('xxxx', page_obj.page_range)
    # # has_previous 上一页？ has_next 下一页 ？
    #
    # for p in page_obj.page_range:
    #     page_i = page_obj.page(p)
    #     print('current page list:  当前是第几页{}'.format(page_i.number), page_i.object_list)

    # value_lists

    ex = models.Examination.objects.all()

    field_list = ['id', 'name', 'course_map', 'invigilator',
                  'read_teacher', 'test_type', 'test_date', 'test_tags']

    ret = generate_result_list(ex, field_list)

    return HttpResponse(json.dumps(ret))
