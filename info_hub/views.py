from urllib import request
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.

from .permissions import IsSchool
from rest_framework.permissions import  IsAuthenticated
from .serializers import *
from .models import *



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsSchool]

    def get_serializer_context(self):
        return {'user': self.request.user }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddPostSerializer
        return PostSerializer

        

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
