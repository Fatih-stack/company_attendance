from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta
from .tasks import send_late_notification
from .models import Attendance, Employee, Leave
from .serializers import AttendanceSerializer, EmployeeSerializer, LeaveSerializer
from django.shortcuts import render

def employee_list(request):
    return render(request, 'employee_list.html')

def attendance_checkin(request):
    return render(request, 'attendance_checkin.html')

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=True, methods=['post'])
    def check_in(self, request, pk=None):
        try:
            employee = self.get_object()
            today = timezone.now().date()
            check_in_time = timezone.now()

            # İlk giriş kaydı
            if not Attendance.objects.filter(employee=employee, check_in_time__date=today).exists():
                Attendance.objects.create(employee=employee, check_in_time=check_in_time)
                
                # Geç kalma kontrolü
                company_start_time = datetime.combine(today, datetime.min.time()) + timedelta(hours=8)
                if check_in_time > company_start_time:
                    late_minutes = (check_in_time - company_start_time).seconds // 60
                    employee.annual_leave_days -= late_minutes / 60 / 8  # Geç kalma süresini yıllık izinden düş
                    employee.save()
                    # Geç kalma bildirimi gönder
                    send_late_notification.delay(employee.user.email)
                
                return Response({'status': 'Checked in successfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'Already checked in today'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
