# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bk_host_innerip', models.CharField(max_length=50)),
                ('bk_os_name', models.CharField(max_length=50)),
                ('bk_host_name', models.CharField(max_length=50)),
                ('bk_cloud_id', models.CharField(max_length=50)),
                ('bk_biz_id', models.CharField(max_length=50)),
                ('bk_host_id', models.CharField(max_length=50)),
                ('bk_mem', models.CharField(max_length=50)),
                ('bk_cpu', models.CharField(max_length=50)),
                ('bk_disk', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HostInfoMonitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bk_host_name', models.CharField(max_length=50)),
                ('bk_biz_id', models.CharField(max_length=50)),
                ('bk_host_innerip', models.CharField(max_length=50)),
                ('bk_host_id', models.CharField(max_length=50)),
            ],
        ),
    ]
