# Generated by Django 2.2.1 on 2019-08-15 02:38

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_event_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=filebrowser.fields.FileBrowseField(blank=True, help_text='Image must be minimum 250px x 250px. Image proportions must be square', max_length=1000, null=True, verbose_name='Event image'),
        ),
    ]