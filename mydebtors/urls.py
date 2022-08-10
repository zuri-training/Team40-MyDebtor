from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *



router = DefaultRouter()

router.register('sponsor', SponsorViewSet )
router.register('student', StudentViewSet, basename='student')
router.register('debt', DebtViewSet)
router.register('biodata', BioDataViewSet, basename='biodata')


urlpatterns =  [

    path('cleared/', cleared_debtors)
] 

urlpatterns +=  router.urls 





