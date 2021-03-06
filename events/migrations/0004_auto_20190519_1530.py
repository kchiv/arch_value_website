# Generated by Django 2.2.1 on 2019-05-19 15:30

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_address',
        ),
        migrations.AddField(
            model_name='event',
            name='event_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='event_state',
            field=localflavor.us.models.USStateField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='event',
            name='event_street',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
