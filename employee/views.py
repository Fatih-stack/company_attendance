from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, Attendance, Leave
from django.contrib.auth.views import LogoutView
from .serializers import EmployeeSerializer, AttendanceSerializer, LeaveSerializer

# Ana Sayfa
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')  # Bu sayfa kullanıcı profil bilgilerini gösterecek

# İzin Talep Etme Sayfası
def leave_request(request):
    return render(request, 'leave_request.html')

# Giriş/Çıkış Yapma Sayfası
def attendance_checkin(request):
    return render(request, 'attendance_checkin.html')

# Çalışan Listesi Sayfası
def employee_list(request):
    return render(request, 'employee_list.html')

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # GET isteğini de POST isteği gibi işleme koyarak çıkış işlemini gerçekleştirir
        return self.post(request, *args, **kwargs)

# API ViewSets
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer