from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from djoser import utils, views
from pyotp import HOTP, random_base32
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .serializers import CustomSocialLoginSerializer, OTPSerializer

# from auth.


class OTPView (APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        global hotp

        hotp = HOTP(random_base32())

        otp = hotp.at(1)

        send_mail(
            subject='New OTP',
            message=f'Your OTP is : {otp}',
            from_email='blazingkrane@gmail.com',
            recipient_list=[request.user.email]
        )

        return Response({"Info": f"otp sent {otp}"})

    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data['otp']
        if hotp.verify(otp, 1):

            user = request.user
            user.is_verified = True
            user.save()
            return Response({"success: 2FA successful "}, status=status.HTTP_202_ACCEPTED)

        return Response("error: invalid otp")


class CustomSocialLoginView(SocialLoginView):
    serializer_class = CustomSocialLoginSerializer


class GoogleLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # CALLBACK_URL_YOU_SET_ON_GOOGLE
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


def google_view(request):

    # This View just gets the code and prints on the terminal.

    code = request.GET.get('code')
    print(f"The code is : {code}")
    print("go to the browser to make a post request")

    """
    # Alternatively, you can send a post request from directly.

    response = requests.post('http://127.0.0.1:8000/dj/google', data={'code': code})
    print("status: " + response.status_code)
    print(response.json()['access_token'])
    """

    return redirect('google-rest')

# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=878674025478-e8s4rf34md8h4n7qobb6mog43nfhfb7r.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline


class LogoutView (views.TokenDestroyView):

    def post(self, request):
        try:
            user = request.user
            user.is_verified = False
            user.save()
        except:
            pass
        utils.logout_user(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
