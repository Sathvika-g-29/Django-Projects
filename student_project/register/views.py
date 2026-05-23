from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned = form.cleaned_data

            student = Student(
                full_name = cleaned['full_name'],
                email = cleaned['email'],
                mobile = cleaned['mobile'],
                dob = cleaned['dob'],
                gender = cleaned['gender'],
                department = cleaned['department'],
                roll_number = cleaned['roll_number'],
                address = cleaned['address'],
                state = cleaned['state'],
                pincode = cleaned['pincode'],
                learning_mode = cleaned['learning_mode'],
                resume = cleaned['resume'],
                about = cleaned['about'],
                agree = cleaned['agree']
            )
            student.save()

           
            return redirect('success')

    else:
        form = StudentRegistrationForm()

    return render(request, "register.html", {"form": form})


def success_page(request):
    
    return render(request, "success.html", {"name": "Student"})
