from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('leave/request/', views.leave_request, name='leave_request'),
    path('attendance/checkin/', views.attendance_checkin, name='attendance_checkin'),
    path('employees/', views.employee_list, name='employee_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]