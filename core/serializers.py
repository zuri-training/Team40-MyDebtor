# from itsdangerous import Serializer
from rest_framework.serializers import ModelSerializer
from .models import *
from djoser.serializers import UserCreatePasswordRetypeSerializer as RegisterSerializer



class CustomUserCreateSerializer (RegisterSerializer):
    class Meta(RegisterSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'NIN', 'password']
        


class SchoolSerializer (ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'reg_number', 'name',
                  'category', 'state', 'LGA', 'logo', 'address', 'user']


class PrincipalSerializer (ModelSerializer):
    class Meta:
        model = Principal
        fields = ['id','name','gender','date_of_birth','address',
                    'id_type', 'id_number','CAC','letter','id_card','user']



