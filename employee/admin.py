from django.contrib import admin
from .models import Employee, Attendance, Leave

# Employee modeli için admin panelinde yönetim
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'email', 'date_joined')
    search_fields = ('name', 'position', 'email')
    list_filter = ('position', 'date_joined')

# Attendance (Katılım) modeli için admin panelinde yönetim
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'check_in_time', 'check_out_time', 'status')
    search_fields = ('employee__name', 'status')
    list_filter = ('status', 'check_in_time')

# Leave (İzin) modeli için admin panelinde yönetim
@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'leave_type', 'start_date', 'end_date', 'status')
    search_fields = ('employee__name', 'leave_type', 'status')
    list_filter = ('leave_type', 'status', 'start_date')
