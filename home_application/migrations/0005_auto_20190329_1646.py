# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_remove_hostinfomonitor_bk_biz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfomonitor',
            name='bk_biz_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostinfomonitor',
            name='bk_cloud_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
