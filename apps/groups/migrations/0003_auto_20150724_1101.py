# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20150724_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 18, 1, 31, 144000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 7, 24, 18, 1, 31, 144000, tzinfo=utc)),
        ),
    ]
