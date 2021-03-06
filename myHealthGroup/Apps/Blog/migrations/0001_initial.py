# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 20:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('Created_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Parent_Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Posted_Date', models.DateTimeField(default=datetime.datetime(2016, 11, 7, 20, 55, 51, 26985, tzinfo=utc))),
                ('Category', models.PositiveSmallIntegerField(choices=[(0, 'General Health'), (1, 'Rare Diseases'), (2, 'Supervision'), (3, 'Other')], default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.Post'),
        ),
    ]
