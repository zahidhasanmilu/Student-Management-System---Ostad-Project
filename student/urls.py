from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),    
    path('students/', views.StudentListView.as_view(), name='all_student'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('student/<int:id>/', views.StudentDetailView.as_view(), name='student_details'),
    path('update/<int:id>/student/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:id>/student/', views.StudentDeleteView.as_view(), name='delete_student'),
    
    path('courses/', views.CourseList.as_view(), name='all_course'),
    path('course_detail/<int:id>/', views.course_detail, name='course_detail'),
    
    path('course_create/', views.CourseCreate.as_view(), name='course_create'), #CourseCreate
    # path('course_create/', views.course_create, name='course_create'),
    path('course_update/<int:id>/', views.CourseUpdate.as_view(), name='course_update'),#CourseUpdate
    # path('course_update/<int:id>/', views.course_update, name='course_update'),
    
    path('course_delete/<int:id>/', views.CourseDelete.as_view(), name='course_delete'), #CourseDelete
    # path('course_delete/<int:id>/', views.course_delete, name='course_delete'), 
    
]