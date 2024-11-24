from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Company Attendance API",
        default_version='v1',
        description="Company employee attendance and leave management API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@company.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),  # Employee uygulamasının URL'lerini dahil et
    path('manager/', include('manager.urls')),  # Manager uygulamasının URL'lerini dahil et
    path('api/', include('employee.api_urls')),  # Employee API URL'leri
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]