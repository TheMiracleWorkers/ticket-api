from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from api.models import Project, Ticket


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 'last_login', 'date_joined']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        verbose_name = 'role'
        fields = ['url', 'name']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']
        read_only = ['tickets']


class TicketSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField('get_project_name')

    def get_project_name(self, ticket):
        if ticket.project:
            return ticket.project.name
        else:
            return 'No Project'

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description',
                  'due_date', 'project', 'project_name', 'priority', 'created_at', 'updated_at']


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
