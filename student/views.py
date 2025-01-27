from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView,CreateView,DeleteView,ListView,UpdateView

from.models import Course, Student

# Create your views here.


class Home(TemplateView):
    template_name = "index.html"
    
    def get_queryset(self):
        students = Student.objects.all()
        courses = Course.objects.all()
        return students
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_queryset()
        context['courses'] = Course.objects.all() 
        return context
    
class StudentListView(ListView):
    model = Student
    template_name = "students/students.html"
    context_object_name = 'students'
    
