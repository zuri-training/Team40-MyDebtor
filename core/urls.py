from django.urls import path
from django.views.generic import TemplateView

from .views import GoogleLogin, LogoutView, OTPView, google_view

urlpatterns = [

    path('', TemplateView.as_view(template_name="core/index.html")),
    path('login/google', GoogleLogin.as_view(), name='google-rest'),
    path('logout', LogoutView.as_view()),
    path('accounts/google/login/callback/', google_view),
    path('otp', OTPView.as_view())
]
