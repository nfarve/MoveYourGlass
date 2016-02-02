# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_auto_20151126_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystats',
            name='date',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
