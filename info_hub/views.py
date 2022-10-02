from likes.views import LikeView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import *
from .permissions import IsSchool
from .serializers import *

# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsSchool]

    def get_serializer_context(self):
        return {'user': self.request.user, 'request' : self.request}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddPostSerializer
        return PostSerializer


class LikePostView (LikeView):
    serializer_class = LikePostSerializer


class CommentViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'user': self.request.user, 'post_id': self.kwargs['post_pk']}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCommentSerializer
        return CommentSerializer


class LikeCommentView(LikeView):
    serializer_class = LikeCommentSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NewsletterViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
