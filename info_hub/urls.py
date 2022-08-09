from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostView)
comments_router = routers.NestedDefaultRouter(router, 'posts', lookup = 'post')
comments_router.register('comments', views.CommentView)

urlpatterns = router.urls + comments_router.urls

