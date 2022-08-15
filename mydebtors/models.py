import os
import random
import string
from datetime import datetime
from uuid import uuid4
from core.models import School

from core.validators import validate_file_size  # Dependecy issue to be resolved later
    
from django.conf import settings
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
# Create your models here.


def get_passport_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('passport/', filename)

def get_complaint_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('complaint/', filename)


def reg_number_generator (length = 10, chars = string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]


class Student (models.Model):


    reg_number = models.CharField(max_length=255, default=reg_number_generator)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null= True , blank=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    student_class = models.CharField(max_length=255)
    passport = models.ImageField(upload_to = get_passport_path, default = 'default.jpg')
    nationality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=550)
    date_of_birth = models.DateField()

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
 
    school = models.ForeignKey(School, on_delete= models.CASCADE, related_name='students')

    def __str__(self) -> str:
        return f'{self.first_name}---{self.reg_number}'

class Sponsor (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    gender = models.CharField(max_length=30, choices=GENDER)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=550)
    NIN = models.CharField(max_length=11)

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='sponsor')




class Debt (models.Model):
   
    CATEGORY = [
            ('tutition', 'tutition'),
            ('damage', 'damage'),
        ]

    STATUS = [
        ('active', 'active'),
        ('pending', 'pending'),
        ('resolved', 'resolved'),

    ]

    TERM = [

        ('first', '1st Term'),
        ('second', '2nd Term'),
        ('third', '3rd Term')
    ]

    id = models.UUIDField(default=uuid4, primary_key=True)
    session = models.CharField(max_length=10)
    term = models.CharField(max_length=20, choices=TERM)
    total_fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    outstanding_fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    category = models.CharField(max_length=255, choices=CATEGORY)
    status = models.CharField(max_length=50, choices=STATUS, default='active')

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='debts')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='debts')


class Complaint (models.Model):

    STATUS = [
        ('cleared', 'cleared'),
        ('pending', 'pending'),
    ]

    description = models.TextField()
    proof = models.FileField(upload_to=get_complaint_path, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['jpg','pdf','png'])],
                                null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='complaints')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name= 'complaints')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints') # The Person making the complaints


