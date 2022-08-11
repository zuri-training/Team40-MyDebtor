from django.core.exceptions import ValidationError
from django.db import IntegrityError
from djoser.serializers import UserCreatePasswordRetypeSerializer as RegisterSerializer
    
from mydebtors.models import Sponsor
from rest_framework.serializers import ModelSerializer

from .models import *


class CustomUserCreateSerializer (RegisterSerializer):
    class Meta(RegisterSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'NIN', 'password']

    def create(self, validated_data):
        try:
            if self.validated_data['NIN'] or self.validated_data['first_name']:
                if not Sponsor.objects.filter(email = self.validated_data['email']).exists():
                    self.fail("cannot_create_user")
                       
            user = self.perform_create(validated_data)

        except IntegrityError:
            self.fail("cannot_create_user")

        return user
        


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



