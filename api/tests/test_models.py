from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Ticket


class TicketTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(title="Test ticket", description="Test Description")

    def test_status_default_unassigned(self):
        ticket = Ticket.objects.first()
        self.assertEqual(ticket.status, 'Unassigned')

    def test_priority_default_1(self):
        ticket = Ticket.objects.first()
        self.assertEqual(ticket.priority, 1)

    def test_add_assigned_user(self):
        ticket = Ticket.objects.first()
        user = User.objects.create_user(username='testuser', password='12345')
        ticket.assigned_user = user
        self.assertEqual(ticket.assigned_user.username, 'testuser')


