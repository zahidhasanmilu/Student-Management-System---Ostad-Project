import os
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import re



def sanitize_filename(filename):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def student_directory_path(instance, filename):
    sanitized_name = sanitize_filename(instance.name)
    return os.path.join('student_images', sanitized_name, filename)

def course_directory_path(instance, filename):
    sanitized_name = sanitize_filename(instance.name)
    return os.path.join('course_images', sanitized_name, filename)


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration = models.IntegerField()
    fee = models.IntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=course_directory_path, default='Course_default.jpg')
    
    def __str__(self):
        return self.name

class Student(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    COUNTRY_CHOICES = (        
        ('Bangladesh', 'Bangladesh'),
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Germany', 'Germany'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(max_length=255,blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    nationality = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=student_directory_path, default='profile_default.png')
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('student_list')
    