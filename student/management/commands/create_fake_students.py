from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from student.models import Student, Course  # `yourapp` আপনার অ্যাপের নাম দিয়ে রিপ্লেস করুন

fake = Faker()

class Command(BaseCommand):
    help = 'Creates fake data for Student model'

    def generate_bd_phone_number(self):
        # বাংলাদেশের ফোন নম্বর প্রিফিক্স (যেমন: 017, 019, 016, ইত্যাদি)
        prefixes = ['017', '019', '016', '014', '015', '013', '018']
        prefix = fake.random_element(elements=prefixes)  # র্যান্ডম প্রিফিক্স বাছাই করুন
        suffix = fake.numerify(text='########')  # ৮ ডিজিটের র্যান্ডম নম্বর তৈরি করুন
        return prefix + suffix  # প্রিফিক্স এবং সাফিক্স যোগ করে ফোন নম্বর তৈরি করুন

    def handle(self, *args, **kwargs):
        courses = Course.objects.all()  # বিদ্যমান কোর্স গুলো নিন
        users = User.objects.all()  # বিদ্যমান ইউজার গুলো নিন

        for _ in range(40):  # ৪০টি ফেক স্টুডেন্ট তৈরি করুন
            Student.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                age=fake.random_int(min=18, max=30),  # 18 থেকে 30 বছর
                address=fake.address(),
                gender=fake.random_element(elements=('Male', 'Female')),
                nationality=fake.random_element(elements=('Bangladesh', 'United States', 'United Kingdom', 'Germany')),
                phone=self.generate_bd_phone_number(),  # কাস্টম ফোন নম্বর ব্যবহার করুন
                course=fake.random_element(elements=courses),  # র্যান্ডম কোর্স বাছাই করুন
                active=fake.boolean(),
                user=fake.random_element(elements=users),  # র্যান্ডম ইউজার বাছাই করুন
                # ফটো ডিফল্ট `profile_default.png` ব্যবহার হবে
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 40 fake students'))