import os
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from .managers import *
from .validators import validate_file_size

# Create your models here.

USER = settings.AUTH_USER_MODEL

# The Abstract User class allows the school to leverage on django's auth system
# and still modify certain fields of choice 

def get_credentials_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('credentials/', filename)


def get_school_logo_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('school_logo/', filename)



class CustomUser(AbstractUser):  

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null= True, blank=True)
    last_name = models.CharField(max_length=255, null= True, blank=True)
    NIN = models.CharField(max_length=11, null=True, blank=True)
    


    objects = CustomBaseManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []


class School (models.Model):

    CATEGORY = ( 
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary')
    )

    # The username should be the school reg. no.

    reg_number = models.CharField(unique=True, max_length= 50 )
    name = models.CharField(max_length=550)
    category = models.CharField(max_length=100, choices=CATEGORY)
    state = models.CharField(max_length=255)
    LGA = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to =get_school_logo_path, default = 'default.jpg')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(USER, on_delete=models.CASCADE)

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
        ("License", "Driver's License" ),
        ("Voters Card","Voters Card"),
        ("Passport", "International Passport")
    )

    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices = GENDER)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=500)
    id_type = models.CharField (max_length=50, choices=SELECT_ID_TYPE)
    id_number = models.CharField(max_length=20)

    CAC     = models.FileField(validators = [validate_file_size, FileExtensionValidator(allowed_extensions=['jpg','pdf','png'])],  upload_to = get_credentials_path, default = 'default_id.png')
    letter  = models.FileField(validators = [validate_file_size, FileExtensionValidator(allowed_extensions=['jpg','pdf','png'])],  upload_to = get_credentials_path, default = 'default_id.png')
    id_card = models.FileField(validators = [validate_file_size, FileExtensionValidator(allowed_extensions=['jpg','pdf','png'])],  upload_to = get_credentials_path, default = 'default_id.png')

    verification = models.BooleanField(default=False)
    