from rest_framework.routers import DefaultRouter
from .views import *
from mydebtors.views import StudentViewSet
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()

router.register('school', SchoolViewSet)
router.register('principal', PrincipalViewSet)

student_router = NestedDefaultRouter(router, 'school', lookup = 'school')

student_router.register('students', StudentViewSet, basename='school-students')

urlpatterns = router.urls + student_router.urls


