# Generated by Django 5.1.5 on 2025-01-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_course_image_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='Course_default.jpg', upload_to='student_directory_path/'),
        ),
    ]
