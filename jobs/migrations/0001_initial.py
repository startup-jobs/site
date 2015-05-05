# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NA', max_length=3, choices=[(b'BAN', b'BANGALORE'), (b'GUR', b'GURGAON'), (b'DEL', b'DELHI'), (b'MUM', b'MUMBAI'), (b'CHE', b'CHENNAI'), (b'PUN', b'PUNE'), (b'NOI', b'NOIDA'), (b'NCR', b'DELHI-NCR'), (b'JAI', b'JAIPUR'), (b'COI', b'COIMBATORE'), (b'HYD', b'HYDERABAD'), (b'AHM', b'AHMEDABAD'), (b'KOL', b'KOLKATA'), (b'GOA', b'GOA'), (b'COC', b'COCHIN'), (b'REM', b'REMOTE'), (b'NA', b'NOT SPECIFIED')])),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'NA', max_length=3, choices=[(b'PRO', b'PROGRAMMING'), (b'ID', b'INTERACTION DESIGN'), (b'GD', b'GRAPHIC DESIGN'), (b'TES', b'TESTING'), (b'SYS', b'SYSTEM ADMINISTRATION'), (b'BIM', b'BUSINESS/MANAGEMENT'), (b'CED', b'WRITER/EDITOR'), (b'CSE', b'CUSTOMER SUPPORT'), (b'MOB', b'MOBILE'), (b'OAD', b'OFFICE ADMINISTRATION'), (b'NA', b'NOT SPECIFIED')])),
            ],
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('post_url', models.CharField(max_length=200)),
                ('job_category', models.ForeignKey(to='jobs.JobCategory')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'NA', max_length=3, choices=[(b'FTE', b'FULL-TIME EMPLOYMENT'), (b'STC', b'SHORT-TERM CONTRACT'), (b'INT', b'INTERSHIP'), (b'FRL', b'FREELANCE/CONSULTING'), (b'VOL', b'VOLUNTEER'), (b'PAR', b'PARTNER'), (b'NA', b'NOT SPECIFIED')])),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('city', models.ForeignKey(to='jobs.City')),
            ],
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='job_type',
            field=models.ForeignKey(to='jobs.JobType'),
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='location',
            field=models.ForeignKey(to='jobs.City'),
        ),
    ]
