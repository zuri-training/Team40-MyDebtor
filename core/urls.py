from django.urls import path
from django.views.generic import TemplateView

from .views import GoogleLogin, google_view

urlpatterns = [
    
    path('', TemplateView.as_view(template_name = "core/index.html")),
    path('dj/google', GoogleLogin.as_view(), name='google-rest'),
    path('accounts/google/login/callback/', google_view )
]






