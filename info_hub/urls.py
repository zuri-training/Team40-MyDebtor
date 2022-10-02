from django.urls import path
from rest_framework_nested import routers

from .views import (CommentViewSet, ContactViewSet, NewsletterViewSet,
                    PostViewSet, LikeCommentView, LikePostView)

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('contact', ContactViewSet)

comments_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
comments_router.register('comments', CommentViewSet, basename='post-comment')


urlpatterns = [
    path('like/post', LikePostView.as_view()),
    path('like/comment', LikeCommentView.as_view())
]
urlpatterns += router.urls + comments_router.urls
