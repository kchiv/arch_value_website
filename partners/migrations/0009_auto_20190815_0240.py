# Generated by Django 2.2.1 on 2019-08-15 02:40

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0008_partner_partner_listing_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_logo',
            field=filebrowser.fields.FileBrowseField(blank=True, help_text='Image must be minimum 250px x 250px. Image proportions must be square', max_length=1000, verbose_name='Partner logo'),
        ),
    ]
