from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()

router.register('sponsor', SponsorViewSet )
router.register('student', StudentViewSet)
router.register('debt', DebtViewSet)


urlpatterns = router.urls
