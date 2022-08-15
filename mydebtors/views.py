from urllib import request
from django_filters.rest_framework import DjangoFilterBackend
from info_hub.permissions import IsSchool
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .paginators import StudentPaginator
from .serializers import *

# Create your views here.
 

class StudentViewSet(ModelViewSet):

    permission_classes = [IsSchool]
    queryset = Student.objects.all().order_by('-date_created').select_related('school').prefetch_related('debts')

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
        return {'school_id': self.kwargs['school_pk']}
    
    # def get_permissions(self):

    #     if self.action == 'retrieve':
    #         self.permission_classes = [IsAuthenticated]

    #     if self.action in ['list', 'create', 'update', 'partial_update']:
    #         self.permission_classes = [IsSchool, IsAdminUser]

    #     if self.action in ['destroy']:
    #         self.permission_classes = [IsAdminUser]
            
    #     return [permission() for permission in self.permission_classes]


class SponsorViewSet (ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['student']
    search_fields  = ['state']


class DebtViewSet (ModelViewSet):

    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            AddDebtorSerializer
        return DebtSerializer


    def get_queryset(self):
        if self.request.user.groups.filter(name ="School"):

            school = School.objects.get(user = self.request.user)
        
        return Debt.objects.filter(school = school)


    def get_serializer_context(self):
        return {'user': self.request.user}


    # def get_permissions(self):

    #     if self.action == 'retrieve':
    #         self.permission_classes = [IsAuthenticated]

    #     if self.action in ['list', 'create', 'update']:
    #         self.permission_classes = [IsSchool, IsAdminUser]

    #     if self.action in ['partial_update', 'destroy']:
    #         self.permission_classes = [IsAdminUser]

    #     return [permission() for permission in self.permission_classes]
    

class BioDataViewSet (ModelViewSet):
    http_method_names=['get', 'head', 'options']
    queryset = Student.objects.all().select_related('sponsor').prefetch_related('debts')
    serializer_class = BioDataSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ComplaintViewSet (ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Complaint.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MakeComplaintSerializer
        return ComplaintSerializer

    def get_serializer_context(self):
        sponsor = Sponsor.objects.filter(email = self.request.user.email).first()

        student, created = Student.objects.get_or_create(sponsor__id = sponsor.id )
        debt = Debt.objects.get(student_id = student.id)
        context={
                    'debt': debt,
                    'user' : self.request.user,
                    'school': student.school
                    
                    }
        return context



#Alternative View And EndPoint

class DebtView (APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
    
    # Debt View For School 

        if request.user.groups.filter(name="School").exists():
            students = Student.objects.filter(school_id = request.user.school)

            serializer = StudentSerializer(students, many = True)

            return Response(serializer.data, status=status.HTTP_200_OK)

    # Debt View For Sponsor/Guardian/Parent
     
        sponsor = Sponsor.objects.filter(email = request.user.email).first()

        student, created = Student.objects.get_or_create(sponsor__id = sponsor.id )

        serializer = StudentSerializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        # Post Data for School to add a Debtor
         
        if request.user.groups.filter(name="School").exists():

            serializer = DebtSerializer(request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        # Post Data for Sponsor/Guardian/Parent To Contend

        
        sponsor = Sponsor.objects.filter(email = self.request.user.email).first()

        student, created = Student.objects.get_or_create(sponsor__id = sponsor.id )
        debt = Debt.objects.get(student_id = student.id)
        serializer = ComplaintSerializer(
            request.data, 
            context={
                    'debt': debt,
                    'user' : request.user,
                    'school': student.school
                    
                    }
            )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



#View To retrieve  a list Cleared Debtors in a particualar school

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cleared_debtors (request):
    school = School.objects.get(user = request.user)
    query = Student.objects.filter(debts__status = 'resolved', school = school)
    serializer = ClearedDebtorsSerializer(query, many = True)

    return Response(serializer.data, status=status.HTTP_200_OK)
