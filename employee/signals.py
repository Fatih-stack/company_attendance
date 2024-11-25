# Personel oluşturulduğunda otomatik olarak 15 gün izin tanımlanması
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Employee
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
        instance.employee.annual_leave_days = 15
        instance.employee.save()

@receiver(post_save, sender=Employee)
def notify_staff_if_leave_below_threshold(sender, instance, **kwargs):
    if instance.annual_leave_days < 3:
        send_mail(
            'Personelin Yıllık İzni Azaldı',
            f'{instance.name} adlı personelin yıllık izni 3 günden azdır.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.STAFF_NOTIFICATION_EMAIL],
            fail_silently=False,
        )