from django.db import models
from employee.models import Leave

# Yönetici (Manager) Modeli
class Manager(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# İzin Onayı (LeaveApproval) Modeli
class LeaveApproval(models.Model):
    APPROVAL_STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending')
    ]

    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    leave = models.OneToOneField(Leave, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=10, choices=APPROVAL_STATUS_CHOICES, default='pending')
    date_approved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.leave.employee.name} - {self.approval_status}"
