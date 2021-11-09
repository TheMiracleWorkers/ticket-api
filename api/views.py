from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.decorators import action


from .models import Ticket, CurrentUser, Project
from .serializers import ProjectSerializer, UserSerializer, GroupSerializer, TicketSerializer, CurrentUserSerializer

from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []
    filterset_fields = ['title', 'description',
                        'due_date', 'project', 'created_at', 'updated_at']


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.   
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []
    filterset_fields = ['name']

    @action(methods=['delete'], detail=True)
    def remove_members(self, request, pk=None):
        project = self.get_object()
        members_to_remove = request.data['members']
        for member in members_to_remove:
            project.members.remove(member)
        return Response(ProjectSerializer(project).data)


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = CurrentUser.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)
