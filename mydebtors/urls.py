from django.urls import path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter


from .views import *

router = DefaultRouter()

router.register('school', SchoolViewSet)
router.register('principal', PrincipalViewSet)
router.register('sponsor', SponsorViewSet )
router.register('biodata', BioDataViewSet, basename='biodata')
router.register('contend', ComplaintViewSet, basename='complaint')
router.register('debt', DebtViewSet)
# router.register('contact-details', ContactViewSet, basename='contact_details')


student_router = NestedDefaultRouter(router, 'school', lookup = 'school')

student_router.register('students', StudentViewSet, basename='school-students')



urlpatterns =  [

    path('cleared', cleared_debtors),

    path('mydebt', DebtView.as_view()),

    path('contact-details', ContactViewSet.as_view(), ),
] 

urlpatterns += router.urls + student_router.urls
















