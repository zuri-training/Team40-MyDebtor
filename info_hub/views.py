from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
# Create your views here.

from . import serializers
from . import models
from .permissions import IsSchool
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import *
from .models import *



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_context(self):
        return {'user': self.request.user }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddPostSerializer
        return PostSerializer


    def get_permissions(self):
        if self.action == 'create': # to create a post
            self.permission_classes = [IsSchool, IsAdminUser]
        if self.action == 'retrieve': # to view a post
            self.permission_classes = [IsSchool | IsAuthenticated | IsAdminUser]
        if self.action == 'list': #to view all posts
            self.permission_classes = [IsSchool]
        if self.action in ['destroy', 'partial_update', 'update']: #to update, delete, and partially update a post
            self.permission_classes = [IsSchool, IsAdminUser]
        return [permission() for permission in self.permission_classes]


class CommentViewSet(ModelViewSet): 

    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Comment.objects.filter(post_id = self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'user': self.request.user , 'post_id' : self.kwargs['post_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCommentSerializer
        return CommentSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NewsletterViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
