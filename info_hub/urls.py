from django.urls import path, include
from rest_framework.routers import DefautRouter

from . import views

router = DefautRouter()
router.register('posts/', views.PostView)
router.register('comments/', views.CommentView)
router.register('contact/', views.ContactView)

urlpatterns = router.urls
