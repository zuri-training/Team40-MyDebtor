from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
# Create your views here.



class SchoolViewSet (ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class PrincipalViewSet (ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer

    