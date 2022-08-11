from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from .paginators import StudentPaginator
from .models import *
from .serializers import *
from info_hub.permissions import IsSchool

# Create your views here.
 

class StudentViewSet(ModelViewSet):

    permission_classes = [IsSchool]
    queryset = Student.objects.filter().select_related('school').prefetch_related('debts')
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['id', 'reg_number']
    pagination_class = StudentPaginator
    search_fields = ['first_name', 'last_name', 'reg_number'] 

    def get_queryset(self):
        
        return Student.objects.filter(school_id = self.kwargs['school_pk']).select_related('school').prefetch_related('debts')
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSerializer
            
        return AddStudentSerializer


    def get_serializer_context(self):
        return {'user' : self.request.user, 'school_id': self.kwargs['school_pk']}
    
    def get_permissions(self):

        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]

        if self.action in ['list', 'create', 'update', 'partial_update']:
            self.permission_classes = [IsSchool, IsAdminUser]

        if self.action in ['destroy']:
            self.permission_classes = [IsAdminUser]
            
        return [permission() for permission in self.permission_classes]


class SponsorViewSet (ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['student']
    search_fields  = ['state']


class DebtViewSet (ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_permissions(self):

        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]

        if self.action in ['list', 'create', 'update']:
            self.permission_classes = [IsSchool, IsAdminUser]

        if self.action in ['partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]

        return [permission() for permission in self.permission_classes]


class BioDataViewSet (ModelViewSet):
    http_method_names=['get', 'head', 'options']
    queryset = Student.objects.all().select_related('sponsor').prefetch_related('debts')
    serializer_class = BioDataSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cleared_debtors (request):
    query = Student.objects.filter(debts__status = 'resolved')
    serializer = ClearedDebtorsSerializer(query, many = True)

    return Response(serializer.data, status=status.HTTP_200_OK)

    
