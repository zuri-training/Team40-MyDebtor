from rest_framework_nested import routers
from . views import PostViewSet, CommentViewSet, NewsletterViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('newsletter', NewsletterViewSet)

comments_router = routers.NestedDefaultRouter(router, 'posts', lookup = 'post')
comments_router.register('comments', CommentViewSet, basename='post-comment')

urlpatterns = router.urls + comments_router.urls

