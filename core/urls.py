from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('school', SchoolViewSet)
router.register('principal', PrincipalViewSet)

urlpatterns = router.urls


