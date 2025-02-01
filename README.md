# Student Management System - Ostad Project

This is a Django-based Student Management System project.

## Getting Started

Follow the steps below to set up and run the project on your local machine.

### Clone the Repository
```bash
git clone https://github.com/zahidhasanmilu/Student-Management-System---Ostad-Project.git
```

### Create and Activate Virtual Environment
```bash
pipenv shell
```

### Navigate to the Project Directory
```bash
cd Student-Management-System---Ostad-Project
```

### Install Required Dependencies
```bash
pipenv install -r requirements.txt
```

### Run Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```
Provide the following credentials when prompted:
- **Username:** `admin`
- **Password:** `123`

### Run the Development Server
```bash
python manage.py runserver
```

### Access the Admin Panel
Open your browser and go to:
```
http://127.0.0.1:8000/admin/
```
Use the superuser credentials to log in.

## Features
- User authentication and authorization
- Student registration and management
- Course
- Admin dashboard

## Technologies Used
- Python
- Django
- SQLite (default database, can be changed)


