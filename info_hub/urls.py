from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
comments_router = routers.NestedDefaultRouter(router, 'posts', lookup = 'post')
comments_router.register('comments', views.CommentViewSet)

urlpatterns = router.urls + comments_router.urls

