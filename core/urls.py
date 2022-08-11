from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from mydebtors.models import Student
from .views import *
from mydebtors.views import StudentViewSet

router = DefaultRouter()

router.register('school', SchoolViewSet)
router.register('principal', PrincipalViewSet)

student_router = NestedDefaultRouter(router, 'school', lookup = 'school')

student_router.register('students', StudentViewSet, basename='school-students')

urlpatterns = router.urls + student_router.urls


