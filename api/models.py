from django.db import models
from rest_framework_jwt.serializers import User


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    due_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
