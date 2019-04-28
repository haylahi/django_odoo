from django.http import HttpResponse
from rest_framework import generics

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

def school_test(request):
    # obj = models.Examination.objects.get(pk=1)
    # obj.create_score_record()

    from school import tasks

    try:
        res = tasks.create_new_record.delay('create_record', data='hello')
        _result = res.get(timeout=0.2)
        print('get celery result {}'.format(_result))
    except Exception as e:
        print('执行失败: {}'.format(e))

    return HttpResponse('<h1>200 Ok</h1>', content_type='text/html', status=200)
