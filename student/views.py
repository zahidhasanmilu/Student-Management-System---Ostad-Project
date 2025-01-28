from django.shortcuts import render, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,UpdateView

from.models import Course, Student
from student.forms import StudentForm
from django.contrib import messages


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
    success_url = reverse_lazy('all_student')  # Redirect to the student list page after successful submission

    # Add the fields attribute
    fields = ['name', 'email', 'age', 'gender', 'phone', 'course', 'nationality', 'address', 'photo', 'active']

    def form_valid(self, form):
        # You don't need to manually assign the data since Django handles this automatically
        # We only need to set the `user` field since it's not part of the form
        form.instance.user = self.request.user  # Set the current user as the owner
        
        # Additional processing for active checkbox
        if 'active' in self.request.POST:
            form.instance.active = True
        else:
            form.instance.active = False
        
        # If needed, you can perform additional validations here
        
        # Call the parent class's form_valid to save the form
        messages.success(self.request, 'Student has been successfully created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add error message to user if the form is invalid
        messages.warning(self.request, 'Student not created. Please check the form.')
        return render(self.request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        # Add available courses to context for the form
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()  # Add all courses for the dropdown
        return context
    
    

class CourseList(ListView):
    model = Course
    context_object_name = 'courses_list'
    template_name='students/courses.html'
