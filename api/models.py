from django.db import models
from rest_framework_jwt.serializers import User


class Project(models.Model):
    name = models.CharField(max_length=60)


class Status(models.Model):
    status = models.CharField(max_length=40)


class PRIORITY_CHOICES(models.IntegerChoices):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    due_date = models.DateTimeField(null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name='tickets', related_query_name='ticket')
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=True, related_name='tickets', related_query_name='ticket')
    priority = models.IntegerField(choices=PRIORITY_CHOICES.choices, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class RegisterUser(models.Model):
    user = ""
