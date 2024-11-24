from django.urls import path
from . import views

urlpatterns = [
    path('leave/approval/', views.leave_approval, name='leave_approval'),
    path('attendance/report/', views.attendance_report, name='attendance_report'),
]