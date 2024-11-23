from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from employee.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leaves', LeaveViewSet)

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
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('attendance/checkin/', attendance_checkin, name='attendance_checkin'),
    path('employees/', employee_list, name='employee_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]