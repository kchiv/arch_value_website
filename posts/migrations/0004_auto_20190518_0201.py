# Generated by Django 2.2.1 on 2019-05-18 02:01

from django.db import migrations, models
import django.utils.timezone
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190518_0117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='header_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modification_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=500, verbose_name='Thumbnail image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=500, verbose_name='Category image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=500, verbose_name='Featured image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Check the box to publish post.'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50),
        ),
    ]
