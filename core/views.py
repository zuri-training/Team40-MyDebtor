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



    


