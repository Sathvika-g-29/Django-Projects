from django.db import models

class Student(models.Model):

    # Personal Details
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    # Academic Details
    department = models.CharField(max_length=20)

    #year = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=20)

    # Address Details
    address = models.TextField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    # Skills & Interestsskills = models.CharField(max_length=200)  # will store as comma-separated string
    learning_mode = models.CharField(max_length=10)

    # Additional Info
    resume = models.FileField(upload_to='resumes/')
    about = models.TextField()
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
