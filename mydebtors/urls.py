from django.urls import path
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()

router.register('sponsor', SponsorViewSet )
router.register('biodata', BioDataViewSet, basename='biodata')
router.register('contend', ComplaintViewSet, basename='complaint')
router.register('debt', DebtViewSet)




urlpatterns =  [

    path('cleared', cleared_debtors),

    path('mydebt', DebtView.as_view())
] 

urlpatterns +=  router.urls 





