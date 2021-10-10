from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    due_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

