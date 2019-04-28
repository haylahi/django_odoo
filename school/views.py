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
