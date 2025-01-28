from django import forms
from student.models import Student, Course


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', )
        
        labels = {
            'name': 'Full Name',
            'course': 'Select Course',
            'email': 'Email',
            'age': 'Age',
            'gender': 'Select Gender',
            'nationality': 'Select Nationality',
            'address': 'Address',
            'phone_number': 'Phone Number',
            'active': 'active',
            'photo': 'Photo',
        }
        
            
            
            
            
    # name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    
    # age = models.IntegerField(blank=True, null=True)
    
    # address = models.TextField(max_length=255,blank=True, null=True)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    
    # nationality = models.CharField(max_length=50, choices=COUNTRY_CHOICES, blank=True, null=True)
    
    # phone = models.CharField(max_length=15)    
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    # photo = models.ImageField(upload_to=student_directory_path, default='profile_default.png')
    # active = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)