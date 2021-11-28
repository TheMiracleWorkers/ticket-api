# Generated by Django 3.2.7 on 2021-11-28 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20211122_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assigned_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', related_query_name='ticketuser', to=settings.AUTH_USER_MODEL),
        ),
    ]