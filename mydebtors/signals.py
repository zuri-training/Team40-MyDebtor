from django.db.models.signals import post_save
from django.dispatch import receiver
from templated_mail.mail import BaseEmailMessage
from core.models import School
from .models import Sponsor


@receiver(post_save, sender = Sponsor )
def send_notification_email(instance, created, **kwargs):
    if created:

        student = instance.student.first_name + " " + instance.student.last_name

        school_id = instance.student.school.id

        school = School.objects.get(user_id = school_id)


        BaseEmailMessage(context={'student': student, 'school': school.name},template_name= 'email/notification.html',).send(to=[instance.email])
                         
                        
                         
