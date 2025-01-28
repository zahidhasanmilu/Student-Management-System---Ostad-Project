from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),    
    path('students/', views.StudentListView.as_view(), name='all_student'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
]