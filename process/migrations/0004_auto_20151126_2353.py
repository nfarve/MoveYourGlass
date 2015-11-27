# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_remove_dailystats_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystats',
            name='sittingTime',
            field=models.CharField(max_length=10000000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dailystats',
            name='suggestionCount',
            field=models.CharField(max_length=10000000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dailystats',
            name='walkingTime',
            field=models.CharField(max_length=10000000),
            preserve_default=True,
        ),
    ]
