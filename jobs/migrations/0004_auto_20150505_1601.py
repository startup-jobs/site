# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150505_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 16, 1, 40, 115298, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 16, 1, 54, 372366, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
