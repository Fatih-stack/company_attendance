from django.test import TestCase
from .models import Employee, Leave

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='John Doe',
            position='Developer',
            email='john.doe@example.com'
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'John Doe')
        self.assertEqual(self.employee.position, 'Developer')
        self.assertEqual(self.employee.email, 'john.doe@example.com')

class LeaveModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name='Jane Doe',
            position='Designer',
            email='jane.doe@example.com'
        )
        self.leave = Leave.objects.create(
            employee=self.employee,
            leave_type='annual',
            start_date='2024-11-01',
            end_date='2024-11-05'
        )

    def test_leave_creation(self):
        self.assertEqual(self.leave.employee.name, 'Jane Doe')
        self.assertEqual(self.leave.leave_type, 'annual')
        self.assertEqual(self.leave.status, 'pending')