# Generated by Django 2.2.1 on 2019-05-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190519_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_partners',
            field=models.ManyToManyField(blank=True, to='partners.Partner'),
        ),
    ]
