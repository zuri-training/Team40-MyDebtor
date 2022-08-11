from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
from . import serializers
from . import models
from .permissions import IsSchool


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_permissions(self):
        if self.action == 'create': # to create a post
            self.permission_classes = [IsSchool, permissions.IsAdminUser]
        if self.action == 'retrieve': # to view a post
            self.permission_classes = [IsSchool | permissions.IsAuthenticated | permissions.IsAdminUser]
        if self.action == 'list': #to view all posts
            self.permission_classes = [IsSchool]
        if self.action in ['destroy', 'partial_update', 'update']: #to update, delete, and partially update a post
            self.permission_classes = [IsSchool, permissions.IsAdminUser]
        return [permission() for permission in self.permission_classes]

class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]



class ContactViewSet(ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


class NewsletterViewSet(ModelViewSet):
    queryset = models.Newsletter.objects.all
    serializer_class = serializers.NewsletterSerializer
