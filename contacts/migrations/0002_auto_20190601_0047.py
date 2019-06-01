# Generated by Django 2.2.1 on 2019-06-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subscriber',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]