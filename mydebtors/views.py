from urllib import request
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from core.models import School

from . models import *
from .serializers import *
# Create your views here.


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['id', 'reg_number']

    def get_queryset(self):
        
        if self.request.method in permissions.SAFE_METHODS:
            return Student.objects.all()
        return Student.objects.filter(school = request.user)

    def get_serializer_context(self):
        return {'user' : self.request.user}


class SponsorViewSet (ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['student']
    search_fields  = ['state']


class DebtViewSet (ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer




class BioDataView (APIView):

    def get(self, request , pk):
        
        serializer = BioDataSerializer(Student, pk)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
