# employee/api_urls.py
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, LeaveViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leaves', LeaveViewSet)

urlpatterns = router.urls
