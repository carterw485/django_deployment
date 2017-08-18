# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20150724_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 20, 30, 30, 647000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 20, 30, 30, 647000, tzinfo=utc)),
        ),
    ]
