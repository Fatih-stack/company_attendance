from django.contrib import admin
from .models import Employee, Attendance, LeaveRequest

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'position', 'email', 'annual_leave_days')
    search_fields = ('name', 'position', 'email')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in_time', 'check_out_time')
    search_fields = ('employee__name', 'date')

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'approved')
    search_fields = ('employee__name', 'start_date', 'end_date')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
