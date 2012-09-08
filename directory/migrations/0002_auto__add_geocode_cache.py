# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Geocode_cache'
        db.create_table('directory_geocode_cache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('directory', ['Geocode_cache'])


    def backwards(self, orm):
        # Deleting model 'Geocode_cache'
        db.delete_table('directory_geocode_cache')


    models = {
        'directory.geocode_cache': {
            'Meta': {'object_name': 'Geocode_cache'},
            'create_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10', 'blank': 'True'})
        },
        'directory.interest': {
            'Meta': {'object_name': 'Interest'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'googleaddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['directory.Interest']", 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '50', 'decimal_places': '10', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '50', 'decimal_places': '10', 'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 7, 0, 0)', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'note': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1500', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'directory.location_hour': {
            'Meta': {'object_name': 'Location_hour'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hclose': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'hopen': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']"})
        },
        'directory.location_operator': {
            'Meta': {'object_name': 'Location_operator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']"}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Operator']"})
        },
        'directory.location_service': {
            'Meta': {'object_name': 'Location_service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Service']"})
        },
        'directory.operator': {
            'Meta': {'object_name': 'Operator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'})
        },
        'directory.perspective': {
            'Meta': {'object_name': 'Perspective'},
            'heading': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']"}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pitch': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10'}),
            'zoom': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10'})
        },
        'directory.project': {
            'Meta': {'object_name': 'Project'},
            'create_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'})
        },
        'directory.report': {
            'Meta': {'object_name': 'Report'},
            'datecreated': ('django.db.models.fields.DateField', [], {}),
            'dateofvisit': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'directory.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['directory']