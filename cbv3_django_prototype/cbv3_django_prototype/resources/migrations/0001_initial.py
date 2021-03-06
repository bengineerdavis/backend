# Generated by Django 2.2.4 on 2020-01-16 23:29

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import resources.models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=300)),
                ('referring_url', models.URLField(blank=True, max_length=300)),
                ('other_referring_source', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('media_type', models.CharField(choices=[('VID', 'Video'), ('POD', 'Podcast'), ('PODEP', 'Podcast Episode'), ('TALK', 'Talk'), ('TUTOR', 'Tutorial'), ('COURSE', 'Course'), ('BOOK', 'Book'), ('BLOG', 'Blog'), ('GAME', 'Game'), ('EVENT', 'Event'), ('TOOL', 'Tool'), ('LIB', 'Library'), ('WEB', 'Website')], max_length=7)),
                ('paid', models.BooleanField(null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=models.SET(resources.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
