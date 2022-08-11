from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
# Create your views here.

from . import serializers
from . import models
from .permissions import IsSchool

from .serializers import *
from .models import *



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {'user': self.request.user }

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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(ModelViewSet): 
    serializer_class = CommentSerializer


    def get_queryset(self):
        return Comment.objects.filter(post_id = self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'user': self.request.user }

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NewsletterViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
