from .models import Student
from django.views.generic.edit import CreateView
from django.contrib import messages
from student.forms import StudentForm, CourseForm
from django.shortcuts import redirect, render, HttpResponse

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView, DetailView

from .models import Course, Student


# Create your views here.

# ------------------Home Dashboard start--------------------------------
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
# ------------------Home Dashboard End--------------------------------




# ------------------Student List Start--------------------------------
class StudentListView(ListView):
    model = Student
    template_name = "students/students.html"
    context_object_name = 'students'
# ------------------Student List End--------------------------------




# ------------------Student Create Start--------------------------------
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
# ------------------Student Create End--------------------------------




# ------------------Student Details Start--------------------------------
class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_details.html"
    context_object_name = 'student'
    pk_url_kwarg = 'id'
# ------------------Student Details End--------------------------------




# ------------------Student Update Start--------------------------------
class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/create_student.html"
    fields = ['name', 'email', 'age', 'gender', 'phone',
              'course', 'nationality', 'address', 'photo', 'active']
    success_url = reverse_lazy('all_student')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        # Check if email already exists
        form.instance.user = self.request.user
        form.instance.active = 'active' in self.request.POST

        # Get the student's name and add a success message
        name = form.instance.name
        messages.success(self.request, f'{
                         name} - Student has been successfully updated!')

        return super().form_valid(form)

    def form_invalid(self, form):
        # Check if the email already exists
        email = form.data.get('email')
        if email and Student.objects.filter(email=email).exclude(pk=self.object.pk).exists():
            messages.error(self.request, f'The email "{
                           email}" is already registered. Please use a different one.')
        # Re-render the form with existing data and errors
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        # Add available courses to context for the form
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['student_updates'] = True
        return context
# ------------------Student Update End--------------------------------




# ------------------Student Delete start--------------------------------
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/delete_student.html"
    success_url = reverse_lazy('all_student')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_deletes'] = True
        return context
# ------------------Student Delete End--------------------------------



# ------------------Course List start--------------------------------
class CourseList(ListView):
    model = Course
    context_object_name = 'courses_list'
    template_name = 'students/courses.html'
# ------------------Course List End--------------------------------




# ------------------Course Details start--------------------------------
def course_detail(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'students/course_details.html', {'course': course})
# ------------------Course Details End--------------------------------


# ------------------Course Create start--------------------------------
class CourseCreate(CreateView):
    model = Course
    template_name = 'students/course_create.html'
    fields = ['name', 'duration', 'fee', 'active', 'image']
    success_url = reverse_lazy('all_course')

    def form_valid(self, form):
        name = form.data.get('name')
        messages.success(self.request, f'{
                         name} - Course has been successfully created!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Course creation failed. Please check the form for errors.")
        return self.render_to_response(self.get_context_data(form=form))


# def course_create(request):
#     # form = CourseForm()
#     if request.method == 'POST':
#         # form = CourseForm(request.POST)
#         name = request.POST.get('name')
#         duration = request.POST.get('duration')
#         fee = request.POST.get('fee')
#         active = request.POST.get('active')
#         image = request.FILES.get('image')

#         if active is not None:
#             active = True
#         else:
#             active = False

#         if not image:
#             image = 'Course_default.jpg'

#         course = Course(
#             name = name,
#             duration = duration,
#             fee = fee,
#             active = active,
#             image = image
#         )
#         course.save()
#         messages.success(request, f'"{name}" Course Created Successfully')
#         return redirect('all_course')
#     return render(request,'students/course_create.html',)
# ------------------Course Create End--------------------------------




# ------------------Course Update start--------------------------------
class CourseUpdate(UpdateView):
    model = Course
    template_name = 'students/course_update.html'
    fields = ['name', 'duration', 'fee', 'active', 'image']
    success_url = reverse_lazy('all_course')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        # Get the course's name and add a success message
        name = form.instance.name
        messages.success(self.request, f'{
                         name} - Course has been successfully updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Re-render the form with existing data and errors
        return self.render_to_response(self.get_context_data(form=form))

# def course_update(request, id):
#     course = Course.objects.get(id=id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         duration = request.POST.get('duration')
#         fee = request.POST.get('fee')
#         active = request.POST.get('active')
#         image = request.FILES.get('image')

#         if active is not None:
#             active = True
#         else:
#             active = False

#         if not image:
#             image = course.image

#         course.name = name
#         course.duration = duration
#         course.fee = fee
#         course.active = active
#         course.image = image
#         course.save()
#         messages.success(request, f'"{name}" Course Updated Successfully')
#         return redirect('all_course')
#     return render(request,'students/course_update.html', {'course': course})

# ------------------Course Update End--------------------------------




# ------------------Course Delete Start--------------------------------

# def course_delete(request, id):
#     course = Course.objects.get(id=id)
#     course.delete()
#     messages.success(request, f'"{course.name}" Course has been deleted successfully')
#     return redirect('all_course')

class CourseDelete(DeleteView):
    model = Course
    template_name = 'students/course_delete.html'
    success_url = reverse_lazy('all_course')
    pk_url_kwarg = 'id'
    context_object_name = 'course'

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, f'"{
                         self.object.name}" Course has been deleted successfully')
        return redirect(self.get_success_url())
# ------------------Course Delete End--------------------------------
