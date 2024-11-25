from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('leave/request/', views.leave_request, name='leave_request'),
    path('attendance/checkin/', views.attendance_checkin, name='attendance_checkin'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/login/', LoginView.as_view(template_name='employee_login.html'), name='employee_login'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
    path('staff/login/', LoginView.as_view(template_name='staff_login.html'), name='staff_login'),
    path('staff/logout/', views.staff_logout, name='staff_logout'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
]