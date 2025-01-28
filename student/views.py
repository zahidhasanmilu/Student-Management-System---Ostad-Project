from .models import Student
from django.views.generic.edit import CreateView
from django.contrib import messages
from student.forms import StudentForm
from django.shortcuts import render, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView

from .models import Course, Student


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


# from django.contrib import messages
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .models import Student, Course


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/create_student.html'
    # Redirect to the student list page after successful submission
    success_url = reverse_lazy('all_student')
    fields = ['name', 'email', 'age', 'gender', 'phone',
              'course', 'nationality', 'address', 'photo', 'active']


    def form_valid(self, form):
        # Check if email already exists
        form.instance.user = self.request.user
        form.instance.active = 'active' in self.request.POST
        name = form.data.get('name')
        # Add a success message
        messages.success(
            self.request, f'{name} - Student has been successfully created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Check if the email already exists
        # Use form.data to retrieve the submitted email
        email = form.data.get('email')
        if email and Student.objects.filter(email=email).exists():
            messages.error(self.request, f'Email "{
                           email}" already exists. Please use a different email.')

        # # Add a general error message
        # messages.error(
        #     self.request, "Student creation failed. Please check the form for errors.")
        # Re-render the form with existing data and errors
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        # Add available courses to context for the form
        context = super().get_context_data(**kwargs)
        # Add all courses for the dropdown
        context['courses'] = Course.objects.all()
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_details.html"
    context_object_name ='student'
    pk_url_kwarg  = 'id'
    

class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/create_student.html"
    fields = ['name', 'email', 'age', 'gender', 'phone', 'course', 'nationality', 'address', 'photo', 'active']
    success_url = reverse_lazy('all_student')
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        # Check if email already exists
        form.instance.user = self.request.user
        form.instance.active = 'active' in self.request.POST
        
        # Get the student's name and add a success message
        name = form.instance.name
        messages.success(self.request, f'{name} - Student has been successfully updated!')
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Check if the email already exists
        email = form.data.get('email')
        if email and Student.objects.filter(email=email).exclude(pk=self.object.pk).exists():
            messages.error(self.request, f'The email "{email}" is already registered. Please use a different one.')
        # Re-render the form with existing data and errors
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        # Add available courses to context for the form
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['student_updates'] = True
        return context
    


class CourseList(ListView):
    model = Course
    context_object_name = 'courses_list'
    template_name = 'students/courses.html'

