from urllib.parse import unquote

from dj_rest_auth.registration.serializers import SocialLoginSerializer
from django.db import IntegrityError
from djoser.serializers import \
    UserCreatePasswordRetypeSerializer as RegisterSerializer
from mydebtors.models import Sponsor
from rest_framework import serializers

from .models import *


class CustomSocialLoginSerializer(SocialLoginSerializer):

    def validate(self, attrs):
        # update the received code to a proper format. so it doesn't throw error.

        attrs['code'] = unquote(attrs.get('code'))

        return super().validate(attrs)


class CustomUserCreateSerializer (RegisterSerializer):
    class Meta(RegisterSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'NIN', 'password']

    def create(self, validated_data):
        try:
            if self.validated_data['NIN'] or self.validated_data['first_name']:
                if not Sponsor.objects.filter(email=self.validated_data['email']).exists():
                    self.fail("cannot_create_user")

            user = self.perform_create(validated_data)

        except IntegrityError:
            self.fail("cannot_create_user")

        return user


class OTPSerializer (serializers.Serializer):
    otp = serializers.CharField(max_length=6)