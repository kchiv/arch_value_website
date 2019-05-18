# Generated by Django 2.2.1 on 2019-05-18 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190517_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=True)),
                ('category_slug', models.SlugField(blank=True, unique=True)),
                ('category_image', filebrowser.fields.FileBrowseField(blank=True, max_length=1000, verbose_name='Category image')),
                ('category_content', tinymce.models.HTMLField(blank=True, verbose_name='Category content')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=300)),
                ('tag_slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post_content',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=1000, verbose_name='Featured image'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=700),
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(to='posts.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_tag',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
    ]