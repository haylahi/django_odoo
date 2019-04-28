# author: Liberty
# date: 2019/4/28 17:05

from django.urls import path

from . import views

urlpatterns = [
    path('school/', views.SchoolListCreateView.as_view()),
    path('grade/', views.GradeListCreateView.as_view()),
    path('course/', views.CourseListCreateView.as_view()),
    path('material/', views.MaterialListCreateView.as_view()),
    path('teacher/', views.TeacherListCreateView.as_view()),
    path('class/', views.ClassListCreateView.as_view()),
    path('course_map/', views.CourseMapListCreateView.as_view()),
    path('examination/', views.ExaminationListCreateView.as_view()),
    path('score/', views.ScoreListCreateView.as_view()),
    path('student/', views.StudentListCreateView.as_view()),
    # ----------------------------------------------------------
    path('test/', views.school_test),
]
