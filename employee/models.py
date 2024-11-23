from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    annual_leave_days = models.IntegerField(default=15)  # Başlangıçta her personele 15 gün izin verilir

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.user.username} - {self.check_in_time}"

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.employee.user.username} - {self.status}"