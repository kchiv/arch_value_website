# Generated by Django 2.2.1 on 2019-05-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190519_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, help_text='Brief description of event.'),
        ),
    ]