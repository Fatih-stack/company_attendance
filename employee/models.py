from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

# Çalışan (Employee) Modeli
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    annual_leave_days = models.IntegerField(default=15)  # İşe başlayan personele 15 gün izin

    def __str__(self):
        return self.user.username
    
class CompanyPolicy:
    START_TIME = datetime.strptime("08:00", "%H:%M").time()
    END_TIME = datetime.strptime("18:00", "%H:%M").time()
    WEEKENDS = [5, 6]  # Cumartesi ve Pazar

# Katılım (Attendance) Modeli
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('on_time', 'On Time'),
        ('late', 'Late'),
        ('absent', 'Absent')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='on_time')

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"
    
    @property
    def is_late(self):
        # Şirketin iş başlangıç saati: 08:00
        company_start_time = CompanyPolicy.START_TIME
        if self.check_in_time and self.check_in_time > company_start_time:
            return True
        return False

    @property
    def working_hours(self):
        # Çalışma saatlerini hesaplamak için
        if self.check_in_time and self.check_out_time:
            check_in = datetime.combine(self.date, self.check_in_time)
            check_out = datetime.combine(self.date, self.check_out_time)
            return (check_out - check_in).seconds / 3600  # Saat cinsinden döner
        return 0

# İzin (Leave) Modeli
class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave')
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"
    
class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def get_approval_url(self):
        return reverse('approve_leave', args=[str(self.id)])

    def __str__(self):
        return f"{self.employee.name} - {self.start_date} to {self.end_date}"
