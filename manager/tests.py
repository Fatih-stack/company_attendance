from django.test import TestCase
from .models import Manager, LeaveApproval
from employee.models import Leave, Employee

class ManagerModelTest(TestCase):
    def setUp(self):
        self.manager = Manager.objects.create(
            name='Alice Smith',
            department='HR',
            email='alice.smith@example.com'
        )

    def test_manager_creation(self):
        self.assertEqual(self.manager.name, 'Alice Smith')
        self.assertEqual(self.manager.department, 'HR')
        self.assertEqual(self.manager.email, 'alice.smith@example.com')

class LeaveApprovalTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='Bob Brown',
            position='Analyst',
            email='bob.brown@example.com'
        )
        self.leave = Leave.objects.create(
            employee=self.employee,
            leave_type='sick',
            start_date='2024-11-10',
            end_date='2024-11-12'
        )
        self.manager = Manager.objects.create(
            name='Charlie White',
            department='Finance',
            email='charlie.white@example.com'
        )
        self.leave_approval = LeaveApproval.objects.create(
            manager=self.manager,
            leave=self.leave,
            approval_status='pending'
        )

    def test_leave_approval_creation(self):
        self.assertEqual(self.leave_approval.manager.name, 'Charlie White')
        self.assertEqual(self.leave_approval.leave.employee.name, 'Bob Brown')
        self.assertEqual(self.leave_approval.approval_status, 'pending')