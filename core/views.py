from django_filters.rest_framework import DjangoFilterBackend
from djoser import utils
from djoser.conf import settings
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.


# class LoginView (TokenCreateView):

#     serializer_class = settings.SERIALIZERS.token_create
#     permission_classes = settings.PERMISSIONS.token_create

#     def _action(self, serializer):
#         token = utils.login_user(self.request, serializer.user)
#         token_serializer_class = settings.SERIALIZERS.token
#         print("HEllo Dumb Dumb")
#         return Response(
#             data=token_serializer_class(token).data, status=status.HTTP_200_OK
#         )




class SchoolViewSet (ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['user', 'address', 'reg_number', 'name', 'id']
    queryset = School.objects.all()
    search_fields = ['user', 'address', 'reg_number', 'name', 'id']
    ordering_fields = ['date_created', 'date_updated']
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes= [IsAuthenticated])
    def me(self, request):
        school, created = School.objects.get_or_create(user = request.user)

        if request.method == 'GET':
            serializer = SchoolSerializer(school)

            return Response(serializer.data , status= status.HTTP_200_OK)
        
        elif request.method == 'PUT':

            serializer = SchoolSerializer(school, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def get_serializer_context(self):
        return {'user': self.request.user}
    

class PrincipalViewSet (ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
    


