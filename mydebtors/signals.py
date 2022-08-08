from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Sponsor
from templated_mail.mail import BaseEmailMessage


@receiver(post_save, sender = Sponsor )
def send_notification_email(instance, created, **kwargs):
    if created:

        student = instance.student.first_name + " " + instance.student.last_name

        BaseEmailMessage(context={'student': student})