from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save, sender=Employee)
def add_initial_leave(sender, instance, created, **kwargs):
    if created:
        instance.annual_leave_days = 15
        instance.save()