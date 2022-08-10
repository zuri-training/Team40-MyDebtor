from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .paginators import StudentPaginator
from .models import *
from .serializers import *

# Create your views here.


class StudentViewSet(ModelViewSet):

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['id', 'reg_number']
    pagination_class = StudentPaginator
    search_fields = ['first_name', 'last_name', 'reg_number'] 

    def get_queryset(self):
        
        if self.request.method in permissions.SAFE_METHODS:
            return Student.objects.all().select_related('user').prefetch_related('debts')
        return Student.objects.filter(school = self.request.user)
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSerializer
            
        return AddStudentSerializer


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




class BioDataViewSet (ModelViewSet):
    http_method_names=['get', 'head', 'options']
    queryset = Student.objects.all().select_related('sponsor').prefetch_related('debts')
    serializer_class = BioDataSerializer
