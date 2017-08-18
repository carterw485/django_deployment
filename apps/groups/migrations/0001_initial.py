# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateField(default=datetime.datetime(2015, 7, 24, 17, 59, 11, 79000, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.ForeignKey(to='groups.Group')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('created_at', models.DateField(default=datetime.datetime(2015, 7, 24, 17, 59, 11, 79000, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='members',
            name='user_id',
            field=models.ForeignKey(to='groups.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(to='groups.User'),
        ),
    ]
