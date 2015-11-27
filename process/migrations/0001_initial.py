# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=25)),
                ('currentDate', models.DateField(auto_now=True, verbose_name=b'last edited')),
                ('previousTotal', models.CharField(max_length=300000)),
                ('currentTotal', models.CharField(max_length=10000)),
                ('x', models.CharField(max_length=10000000)),
                ('y', models.CharField(max_length=10000000)),
                ('z', models.CharField(max_length=10000000)),
                ('resultOn', models.CharField(max_length=10000000)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('walkingTime', models.IntegerField()),
                ('sittingTime', models.IntegerField()),
                ('suggestionCount', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
