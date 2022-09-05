from uuid import uuid4

from django.conf import settings
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models

from .path_helpers import *
from .validators import validate_file_size

# Create your models here.


USER = settings.AUTH_USER_MODEL


GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class School (models.Model):

    CATEGORY = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary')
    )

    # The username should be the school reg. no.

    reg_number = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=550)
    category = models.CharField(max_length=100, choices=CATEGORY)
    state = models.CharField(max_length=255)
    LGA = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    logo = models.ImageField(
        upload_to=get_school_logo_path, default='default.jpg')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        USER, on_delete=models.CASCADE, related_name='school')

    def __str__(self) -> str:
        return self.name


class Principal (models.Model):

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    # using first letter for gender choice
    SELECT_ID_TYPE = (
        ('NIN', 'National Identity Number'),
        ("License", "Driver's License"),
        ("Voters Card", "Voters Card"),
        ("Passport", "International Passport")
    )

    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=500)
    id_type = models.CharField(max_length=50, choices=SELECT_ID_TYPE)
    id_number = models.CharField(max_length=20)

    CAC = models.FileField(validators=[validate_file_size, FileExtensionValidator(allowed_extensions=[
                           'jpg', 'pdf', 'png'])],  upload_to=get_credentials_path, default='default_id.png')
    letter = models.FileField(validators=[validate_file_size, FileExtensionValidator(allowed_extensions=[
                              'jpg', 'pdf', 'png'])],  upload_to=get_credentials_path, default='default_id.png')
    id_card = models.FileField(validators=[validate_file_size, FileExtensionValidator(
        allowed_extensions=['jpg', 'pdf', 'png'])],  upload_to=get_credentials_path, default='default_id.png')

    verification = models.BooleanField(default=False)


class Student (models.Model):

    reg_number = models.CharField(max_length=255, default=reg_number_generator)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER)
    student_class = models.CharField(max_length=255)
    passport = models.ImageField(
        upload_to=get_passport_path, default='default.jpg')
    nationality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=550)
    date_of_birth = models.DateField()

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students')

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

    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name='sponsor')


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
    total_fee = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    outstanding_fee = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    category = models.CharField(max_length=255, choices=CATEGORY)
    status = models.CharField(max_length=50, choices=STATUS, default='active')

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='debts')
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='debts')


class Complaint (models.Model):

    STATUS = [
        ('cleared', 'cleared'),
        ('pending', 'pending'),
    ]

    description = models.TextField()
    proof = models.FileField(upload_to=get_complaint_path, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['jpg', 'pdf', 'png'])],
                             null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

    debt = models.ForeignKey(
        Debt, on_delete=models.CASCADE, related_name='complaints')
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='complaints')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='complaints')  # The Person making the complaints
