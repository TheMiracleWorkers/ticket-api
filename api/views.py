from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import Ticket, CurrentUser
from .serializers import UserSerializer, GroupSerializer, TicketSerializer, CurrentUserSerializer

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
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []
    filterset_fields = ['title', 'description', 'due_date', 'created_at', 'updated_at']


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = CurrentUser.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)

