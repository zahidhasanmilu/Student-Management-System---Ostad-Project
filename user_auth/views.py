import re
from django.shortcuts import redirect, render, HttpResponse
from student.models import Student
from student.forms import StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate username
        if len(name) < 3 or len(name) > 15:
            messages.info(
                request, "Username must be between 3 and 15 characters.")
            print("Username must be between 3 and 15 characters.")
            return redirect('user_signup')

        # Check if username starts with a letter and contains only alphanumeric characters
        # Regex pattern:
        username_pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'

        if not re.match(username_pattern, name):
            messages.info(
                request, "Username must start with a letter and contain only letters and numbers.")
            print(
                "Username must start with a letter and contain only letters and numbers.")
            return redirect('user_signup')

        # Password length validation (maximum 3 characters)
        if len(password) < 3:
            messages.info(
                request, "Password must be at least 3 characters long.")
            print("Password must be minimum at least 3 characters long")
            return redirect('user_signup')

        if password == confirm_password:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'User Already Exists')
                print('User already exists')
                return redirect('user_signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                print('Email already exists')
                return redirect('user_signup')
            else:
                obj = User.objects.create_user(
                    username=name, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Succefully')
                return HttpResponse('successfully created')
        else:
            messages.info(request, "password doesn't match")
            return redirect('user_signup')
    return render(request, 'user_auth/signup.html')


def user_login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username exists in the database
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist.')
            return redirect('user_login')
        
        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('index')
        else:
            # Check if the password is incorrect
            user_obj = User.objects.filter(username=username).first()
            if user_obj is not None and not user_obj.check_password(password):
                messages.error(request, 'Invalid password.')
            else:
                messages.error(request, 'Invalid username or password.')
    
    return render(request, 'user_auth/login.html')

# def user_logout(request):
#     logout(request)
#     messages.success(request, 'Logged out successfully')
#     return redirect('user_login')
