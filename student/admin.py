from django.contrib import admin
from student.models import Course, Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','name', 'email', 'phone', 'course', 'photo', 'active', 'user', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'phone', 'course', 'photo', 'active', 'user', 'created_at', 'updated_at']
    list_filter = ['name', 'email', 'phone', 'course', 'photo', 'active', 'user', 'created_at', 'updated_at']
    list_editable = ['email', 'phone', 'course', 'photo', 'active', 'user',]
    list_display_links = ['name']
    list_per_page = 10
    date_hierarchy = 'created_at'

        
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'fee', 'active', 'image']
    search_fields = ['name', 'duration', 'fee', 'active']
    list_filter = ['name', 'duration', 'fee', 'active']
    list_editable = ['duration', 'fee', 'active']
    list_display_links = ['name']
    list_per_page = 10


admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)