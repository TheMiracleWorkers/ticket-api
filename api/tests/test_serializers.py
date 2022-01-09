from django.contrib.auth.models import User
from django.test import TestCase

from api.models import Ticket, Project
from api.serializers import TicketSerializer


class TestTicketSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(title="Test ticket", description="Test Description")

    def get_serializer(self):
        ticket = Ticket.objects.first()
        return TicketSerializer(ticket)

    def test_contains_expected_fields(self):
        serializer = self.get_serializer()
        data = serializer.data

        self.assertEqual(set(data.keys()), {'id', 'title', 'description',
                                            'due_date', 'project', 'project_name', 'status', 'priority',
                                            'assigned_user', 'assigned_username', 'created_at', 'updated_at'})

    def test_displays_no_user_if_no_assinged_user(self):
        serializer = self.get_serializer()
        data = serializer.data

        self.assertEqual(data['assigned_username'], 'No User')

    def test_displays_username_if_assigned_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        ticket = Ticket.objects.first()
        ticket.assigned_user = user
        ticket.save()

        serializer = self.get_serializer()
        data = serializer.data

        self.assertEqual(data['assigned_username'], user.username)

    def test_displays_no_project_if_no_project(self):
        serializer = self.get_serializer()
        data = serializer.data

        self.assertEqual(data['project_name'], 'No Project')

    def test_displays_project_name_if_project(self):
        project = Project.objects.create(name='Test Project')
        ticket = Ticket.objects.first()
        ticket.project = project
        ticket.save()

        serializer = self.get_serializer()
        data = serializer.data

        self.assertEqual(data['project_name'], project.name)

