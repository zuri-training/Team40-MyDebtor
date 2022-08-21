from django.db import IntegrityError
from djoser.serializers import UserCreatePasswordRetypeSerializer as RegisterSerializer
    
from mydebtors.models import Sponsor

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
        




