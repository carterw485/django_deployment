# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 18, 1, 1, 235000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 18, 1, 1, 235000, tzinfo=utc)),
        ),
    ]
