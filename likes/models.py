from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class LikesManager(models.Manager):
    def get_likes_for (self, content_object, object_id):
        query = ContentType.objects.get_for_model(content_object, object_id)
        return query

class LikedItem(models.Model):
    objects = LikesManager
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

