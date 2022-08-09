from django.shortcuts import render
from rest_framework.viewswets import ModelViewSet

# Create your views here.
from . import serializers
from . import models


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class NewsletterView(ModelViewSet):
    queryset = Newsletter.objects.all
    serializer_class = serializers.NewsletterSerializer
