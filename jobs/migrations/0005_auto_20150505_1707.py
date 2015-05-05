# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150505_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobprofile',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='modified',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='type',
            field=models.CharField(max_length=200),
        ),
    ]
