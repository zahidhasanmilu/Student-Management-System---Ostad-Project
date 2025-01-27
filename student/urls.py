from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),    
    path('students/', views.StudentListView.as_view(), name='all_student'),
]