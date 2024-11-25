from django.shortcuts import render, redirect
from rest_framework import viewsets
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from .models import Employee, Attendance, Leave, CompanyPolicy, LeaveRequest
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout as auth_logout
from .serializers import EmployeeSerializer, AttendanceSerializer, LeaveSerializer

# Giriş ve çıkış kayıtlarını tutmak için view
def check_in(request):
    employee = Employee.objects.get(user=request.user)
    today = datetime.date.today()
    attendance, created = Attendance.objects.get_or_create(employee=employee, date=today)
    if today.weekday() in CompanyPolicy.WEEKENDS:
        return redirect('home')  # Tatil günlerinde check-in yapılmasına izin verilmez
    if not attendance.check_in_time:
        attendance.check_in_time = now().time()
        attendance.save()
        # Eğer geç kaldıysa izin kesintisi yap
        if attendance.is_late:
            late_minutes = (datetime.combine(today, attendance.check_in_time) - datetime.combine(today, CompanyPolicy.START_TIME)).seconds // 60
            employee.annual_leave_days -= late_minutes / 60 / 8  # Her 8 saatlik geç kalma için 1 günlük izin kesintisi
            employee.save()
    return redirect('home')

def check_out(request):
    employee = Employee.objects.get(user=request.user)
    today = datetime.date.today()
    try:
        attendance = Attendance.objects.get(employee=employee, date=today)
        if not attendance.check_out_time:
            attendance.check_out_time = now().time() if now().time() <= CompanyPolicy.END_TIME else CompanyPolicy.END_TIME
            attendance.save()
    except Attendance.DoesNotExist:
        # Eğer personel check-in yapmadıysa check-out yapılamaz
        pass
    return redirect('home')

# Yetkili kişinin tüm personelin giriş/çıkış kayıtlarını görüntüleyebileceği view
def attendance_report(request):
    if request.user.is_staff:
        attendances = Attendance.objects.all().order_by('-date')
        late_attendances = [attendance for attendance in attendances if attendance.is_late]
        return render(request, 'attendance_report.html', {'attendances': attendances, 'late_attendances': late_attendances})
    return redirect('home')

def leave_request(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        LeaveRequest.objects.create(employee=request.user.employee, start_date=start_date, end_date=end_date)
        return redirect('employee_leaves')
    return render(request, 'leave_request.html')

def approve_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    if request.user.is_staff:
        leave.approved = True
        leave.save()
    return redirect('staff_dashboard')

# Personel için izin raporu
def leave_report(request):
    employee = Employee.objects.get(user=request.user)
    leave_requests = LeaveRequest.objects.filter(employee=employee)
    return render(request, 'leave_report.html', {'leave_requests': leave_requests})

def reject_leave(request, leave_id):
    leave = LeaveRequest.objects.get(id=leave_id)
    if request.user.is_staff:
        leave.approved = False
        leave.save()
    return redirect('staff_dashboard')

def notify_staff_about_late(employee, attendance):
    if attendance.is_late:
        send_mail(
            'Personel Geç Kaldı',
            f'{employee.name} bugün işe geç kalmıştır. Giriş saati: {attendance.check_in_time}.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.STAFF_NOTIFICATION_EMAIL],
            fail_silently=False,
        )

# Aylık çalışma saatleri raporu view
def monthly_work_report(request):
    if request.user.is_authenticated:
        employee = Employee.objects.get(user=request.user)
        current_month = datetime.date.today().month
        attendances = Attendance.objects.filter(employee=employee, date__month=current_month)
        total_hours = sum([attendance.working_hours for attendance in attendances])
        return render(request, 'monthly_work_report.html', {'total_hours': total_hours, 'attendances': attendances})
    return redirect('home')

# Şirketin tatil günleri ve izin yönetimi
def is_working_day(date):
    # Cumartesi ve Pazar tatil günleri
    return date.weekday() not in [5, 6]

# Ana Sayfa
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')  # Bu sayfa kullanıcı profil bilgilerini gösterecek

# Yetkili için izin ekleme view
def add_leave(request):
    if request.user.is_staff:
        if request.method == 'POST':
            # İzin tanımlama form işlemleri
            pass
        return render(request, 'add_leave.html')
    return redirect('home')

# Giriş/Çıkış Yapma Sayfası
def attendance_checkin(request):
    return render(request, 'attendance_checkin.html')

# Çalışan Listesi Sayfası
def employee_list(request):
    return render(request, 'employee_list.html')

def employee_leaves(request):
    leaves = LeaveRequest.objects.filter(employee=request.user.employee)
    return render(request, 'employee_leaves.html', {'leaves': leaves})

def assign_leave(request, employee_id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=employee_id)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        LeaveRequest.objects.create(employee=employee, start_date=start_date, end_date=end_date, approved=True)
        return redirect('staff_dashboard')
    return render(request, 'assign_leave.html')

# Logout Sayfası
def employee_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')  # Çıkış yaptıktan sonra yönlendirilecek sayfa
    return render(request, 'employee_logout.html')

# Logout Sayfası
def staff_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')  # Çıkış yaptıktan sonra yönlendirilecek sayfa
    return render(request, 'staff_logout.html')

def staff_dashboard(request):
    if request.user.is_staff:
        attendances = Attendance.objects.filter(check_in_time__isnull=False)
        context = {
            'attendances': [
                {
                    'employee': attendance.employee,
                    'date': attendance.date,
                    'check_in_time': attendance.check_in_time,
                    'is_late': attendance.is_late()
                } for attendance in attendances
            ]
        }
        return render(request, 'staff_dashboard.html', context)
    else:
        return redirect('staff/login')

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
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