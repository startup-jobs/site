# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150505_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcategory',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jobprofile',
            name='post_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='type',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='url',
            field=models.URLField(),
        ),
    ]
