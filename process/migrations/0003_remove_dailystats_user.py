# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_auto_20151126_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailystats',
            name='user',
        ),
    ]
