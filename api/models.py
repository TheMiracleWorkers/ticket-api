from django.db import models
from rest_framework_jwt.serializers import User
from multiselectfield import MultiSelectField

class Project(models.Model):
    name = models.CharField(max_length=60)

Priority_CHOICES = (
    ('HIGH', '1'),
    ('MEDIUM', '2'),
    ('LOW', '3'),
    )

class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    due_date = models.DateTimeField(null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name='tickets', related_query_name='ticket')
    priority = models.CharField(max_length=10, choices=Priority_CHOICES, default ='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    


class CurrentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
