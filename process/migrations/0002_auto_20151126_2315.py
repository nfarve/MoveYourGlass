# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='reporter',
        ),
        migrations.AddField(
            model_name='dailystats',
            name='userid',
            field=models.CharField(default='test', max_length=15),
            preserve_default=False,
        ),
    ]
