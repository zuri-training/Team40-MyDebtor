from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
from . import serializers
from . import models


class PostView(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentView(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class ContactView(ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class NewsletterView(ModelViewSet):
    queryset = models.Newsletter.objects.all
    serializer_class = serializers.NewsletterSerializer
