from django.contrib import admin

# Register your models here.
from info_hub.models import *

admin.site.register([Post, Comment, Contact, Newsletter])
# admin.site.register(models.Post)
# admin.site.register(models.Comment)
# admin.site.register(models.Contact)
# admin.site.register(models.Newsletter)
