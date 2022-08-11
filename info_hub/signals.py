from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Newsletter

@receiver(signal=post_save, sender = settings.AUTH_USER_MODEL)
def add_user_to_newsletter_table(instance, created, sender, **kwargs):
    if created:
        
        if instance.email != '':
            Newsletter.objects.create(email=instance.email)
        

            

        
