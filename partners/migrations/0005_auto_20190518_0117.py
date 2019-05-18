# Generated by Django 2.2.1 on 2019-05-18 01:17

from django.db import migrations
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20190518_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Partner description'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_logo',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=1000, verbose_name='Partner logo'),
        ),
    ]
