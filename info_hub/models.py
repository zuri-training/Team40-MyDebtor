from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Post(models.Model):

    content = models.TextField()
    attachment = models.FileField(validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'png', 'mp4', 'mkv'])], null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.content[:]


class Comment(models.Model):

    content = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Contact (models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter (models.Model):

    email = models.EmailField()
