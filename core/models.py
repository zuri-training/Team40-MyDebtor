from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator
from django.db import models

from .managers import CustomBaseManager

# Create your models here.



# The Abstract User class allows the school to leverage on django's auth system
# and still modify certain fields of choice 




class CustomUser(AbstractUser):  

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null= True, blank=True)
    last_name = models.CharField(max_length=255, null= True, blank=True)
    NIN = models.CharField(max_length=11, validators=[MinLengthValidator(11)], null=True, blank=True)

    is_verified = models.BooleanField(default = False)
    
 

    objects = CustomBaseManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

class AuthSettings (models.Model):
    google_auth = models.BooleanField()
    mobile_verification = models.BooleanField()

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'auth_settings' )
    
class NotificationSettings(models.Model):
    on_comments = models.BooleanField()
    on_likes = models.BooleanField()

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'notification_settings' )

