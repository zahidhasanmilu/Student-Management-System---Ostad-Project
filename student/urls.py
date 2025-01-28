from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),    
    path('students/', views.StudentListView.as_view(), name='all_student'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('student/<int:id>/', views.StudentDetailView.as_view(), name='student_details'),
    path('update/<int:id>/student/', views.StudentUpdateView.as_view(), name='update_student'),
    path('courses/', views.CourseList.as_view(), name='all_course'),
]