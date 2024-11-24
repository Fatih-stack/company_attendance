from django.shortcuts import render
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# İzin Onaylama Sayfası
def leave_approval(request):
    return render(request, 'leave_approval.html')

# Çalışma Saati Raporları Sayfası
def attendance_report(request):
    return render(request, 'attendance_report.html')