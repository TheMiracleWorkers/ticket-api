from django.db import models
from rest_framework_jwt.serializers import User
from django.contrib.auth.models import User as Django_User


class Project(models.Model):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_project', related_query_name='owned_project')
    members = models.ManyToManyField(User, related_name='projects', related_query_name='project', blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    due_date = models.DateTimeField(null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name='tickets', related_query_name='ticket')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
