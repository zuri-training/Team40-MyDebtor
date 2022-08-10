from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
from . import serializers
from . import models


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer



class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer



class ContactViewSet(ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class NewsletterViewSet(ModelViewSet):
    queryset = models.Newsletter.objects.all
    serializer_class = serializers.NewsletterSerializer
