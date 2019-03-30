# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_hostinfo_hostinfomonitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfomonitor',
            name='bk_biz_id',
        ),
    ]
