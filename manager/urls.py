from django.urls import path
from . import views

urlpatterns = [
    path('leave/approval/', views.leave_approval, name='leave_approval'),
    path('attendance/report/', views.attendance_report, name='attendance_report'),
]


# employee/api_urls.py
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeViewSet, AttendanceViewSet, LeaveViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leaves', LeaveViewSet)

urlpatterns = router.urls