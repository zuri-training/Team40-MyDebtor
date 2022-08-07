from django.db import models
from django.conf import settings
from datetime import timezone
# Create your models here.


class Student (models.Model):

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    reg_number = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null= True , blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    student_class = models.CharField(max_length=255)
    passport = models.ImageField(upload_to = 'passport', default = '')
    school = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)



class Contact (models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField
    date = models.DateTimeField(auto_now_add=True)