
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi #
from drf_yasg.views import get_schema_view


schema_view = get_schema_view( # new
    openapi.Info(
        title="CHECKLIST API",
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),


    path('swagger/', schema_view.with_ui( # new
    'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
    'redoc', cache_timeout=0), name='schema-redoc'),
]
