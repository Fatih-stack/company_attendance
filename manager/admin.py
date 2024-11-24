from django.contrib import admin
from .models import Manager, LeaveApproval

# Manager modeli için admin panelinde yönetim
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'email')
    search_fields = ('name', 'department', 'email')
    list_filter = ('department',)

# LeaveApproval (İzin Onayı) modeli için admin panelinde yönetim
@admin.register(LeaveApproval)
class LeaveApprovalAdmin(admin.ModelAdmin):
    list_display = ('id', 'manager', 'leave', 'approval_status', 'date_approved')
    search_fields = ('manager__name', 'leave__employee__name', 'approval_status')
    list_filter = ('approval_status', 'date_approved')
