from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serializers import *
from djoser.views import TokenCreateView, TokenDestroyView
from djoser import utils
from djoser.conf import settings
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# class LoginView (TokenCreateView):

#     def _action(self, serializer):
#         token = utils.login_user(self.request, serializer.user)
#         token_serializer_class = settings.SERIALIZERS.token

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



    

class PrincipalViewSet (ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer



