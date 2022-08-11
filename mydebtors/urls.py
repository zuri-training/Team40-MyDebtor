from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()

router.register('sponsor', SponsorViewSet )
router.register('student', StudentViewSet, basename='student')
router.register('debt', DebtViewSet)
router.register('biodata', BioDataViewSet, basename='biodata')




urlpatterns =  [

    path('cleared/', cleared_debtors)
] 

urlpatterns +=  router.urls 





