from django.shortcuts import render

# İzin Onaylama Sayfası
def leave_approval(request):
    return render(request, 'leave_approval.html')

# Çalışma Saati Raporları Sayfası
def attendance_report(request):
    return render(request, 'attendance_report.html')