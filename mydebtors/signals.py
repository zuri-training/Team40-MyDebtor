from django.db.models.signals import post_save
from django.dispatch import receiver
from templated_mail.mail import BaseEmailMessage

from .models import Sponsor


@receiver(post_save, sender = Sponsor )
def send_notification_email(instance, created, **kwargs):
    if created:

        student = instance.student.first_name + " " + instance.student.last_name

        BaseEmailMessage(context={'student': student})
