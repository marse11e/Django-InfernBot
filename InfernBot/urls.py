from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Infern Bot API Documentation",
        default_version='v1',
        description="Telegram Bot and Django Rest Framework API documentation",
        terms_of_service="https://www.itcbootcamp.com/info_pages/privacy_policy",
        
        contact=openapi.Contact(
            name="Marselle Naz",
            url="https://instagram.com/marselle.naz",
            email="marselle.naz@yandex.kz",
        ),    
        
        license=openapi.License(
            name="MIT License",
            url="https://opensource.org/licenses/MIT",
        ),   
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('main.urls')), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('redoc/', include('django.contrib.admindocs.urls')),
]
