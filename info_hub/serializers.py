from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    content = serializers.TextField()
    attachment = serializers.FileField(validators=[FileExtensionValidator(
        allowed_extensions=['jpg', 'png', 'mp4', 'mkv'])], null=True, blank=True)
    user = serializers.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='posts')
    date_created = serializers.DateTimeField(auto_now_add=True)

    class Meta:
        model = Post
        fields = ['content', 'attachment', 'user', 'date_created']


class CommentSerializer(serializers.ModelSerializer):
    content = serializers.TextField()
    post = serializers.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    user = serializers.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='comments')
    date_created = serializers.DateTimeField(auto_now_add=True)

    class Meta:
        model = Comment
        fields = ['content', 'post', 'user', 'date_created']


class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    message = serializers.TextField()
    date = serializers.DateTimeField(auto_now_add=True)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date']


class NewsletterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Newsletter
        fields = ['email']
