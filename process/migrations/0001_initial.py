# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'process_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userId', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('currentDate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('previousTotal', self.gf('django.db.models.fields.CharField')(max_length=300000)),
            ('currentTotal', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('x', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10000000)),
            ('y', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10000000)),
            ('z', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10000000)),
            ('resultOn', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10000000)),
        ))
        db.send_create_signal(u'process', ['Activity'])

        # Adding model 'Activity2'
        db.create_table(u'process_activity2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userId', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('currentDate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('previousTotal', self.gf('django.db.models.fields.CharField')(max_length=300000)),
            ('currentTotal', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('resultOn', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=10000000)),
        ))
        db.send_create_signal(u'process', ['Activity2'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'process_activity')

        # Deleting model 'Activity2'
        db.delete_table(u'process_activity2')


    models = {
        u'process.activity': {
            'Meta': {'object_name': 'Activity'},
            'currentDate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'currentTotal': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previousTotal': ('django.db.models.fields.CharField', [], {'max_length': '300000'}),
            'resultOn': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000000'}),
            'userId': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'x': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000000'}),
            'y': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000000'}),
            'z': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000000'})
        },
        u'process.activity2': {
            'Meta': {'object_name': 'Activity2'},
            'currentDate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'currentTotal': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previousTotal': ('django.db.models.fields.CharField', [], {'max_length': '300000'}),
            'resultOn': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '10000000'}),
            'userId': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['process']