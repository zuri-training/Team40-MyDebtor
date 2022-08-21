from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from templated_mail.mail import BaseEmailMessage

from .models import School, Sponsor


@receiver(post_save, sender = Sponsor )
def send_notification_email(instance, created, **kwargs):
    if created:

        student = instance.student.first_name + " " + instance.student.last_name

        school_id = instance.student.school.id

        school = School.objects.get(id = school_id)


        BaseEmailMessage(context={'student': student, 'school': school.name},template_name= 'email/notification.html',).send(to=[instance.email])
                         
                        


@receiver(signal=post_save, sender = settings.AUTH_USER_MODEL)
def add_user_to_group(instance, created, sender, **kwargs):
    if created:
        
        if not Group.objects.filter(name = 'School').exists():

            Group.objects.create(name = 'School')
            Group.objects.create(name = 'Parent')

            

        if instance.NIN == "":
            school_group = Group.objects.get(name = 'School')

            instance.groups.add(school_group)
        
    
        else:
            parent_group = Group.objects.get(name = 'Parent') 
            instance.groups.add(parent_group)



@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_school (instance, created, **kwargs):
    if created:

        if instance.NIN == "":
            School.objects.create(user = instance)
