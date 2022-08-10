from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('school', SchoolViewSet)
router.register('principal', PrincipalViewSet)

urlpatterns = router.urls


