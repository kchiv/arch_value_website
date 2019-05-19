# Generated by Django 2.2.1 on 2019-05-18 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190518_0511'),
        ('partners', '0005_auto_20190518_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_tag',
            field=models.ForeignKey(blank=True, help_text='Select tag for the partner if it exists. This will populate blog posts with that tag.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Tag'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_url',
            field=models.URLField(blank=True, help_text='Enter the URL for partner website.'),
        ),
    ]