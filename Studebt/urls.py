from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
# from core.views import LoginView

# customize the django admin with Studebt Admin
admin.site.site_header = 'Studebt Admin'

schema_view = get_schema_view(
    openapi.Info(
        title="Studebt API",
        default_version='v1',
        description="A web based application that helps schools keep track of student's credit history.",
        terms_of_service="https://www.studebt.com/policies/terms/",
        contact=openapi.Contact(email="studebt4@gmail.com"),
        license=openapi.License(name="Studebt License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # path('', include('core.urls')),

    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),

    # path('login/', LoginView.as_view()),

    path('__debug__/', include('debug_toolbar.urls')),
    
    path('', include ('mydebtors.urls')),

    # linking info_hub urls
    path('', include ('info_hub.urls')),


    # path('biodata/<int:pk>', BioDataView.as_view()),



    #Documentation Links
    
   # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)