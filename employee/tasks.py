from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_late_notification(email):
    send_mail(
        'Geç Giriş Uyarısı',
        'Geç kaldığınız için bilgilendirildiniz.',
        'admin@company.com',
        [email],
        fail_silently=False,
    )