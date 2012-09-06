# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Interest'
        db.create_table('directory_interest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('directory', ['Interest'])

        # Adding model 'Location'
        db.create_table('directory_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('interest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Interest'], blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=1500, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10, blank=True)),
            ('googleaddress', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('mod_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 5, 0, 0), blank=True)),
        ))
        db.send_create_signal('directory', ['Location'])

        # Adding model 'Operator'
        db.create_table('directory_operator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('link', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True)),
        ))
        db.send_create_signal('directory', ['Operator'])

        # Adding model 'Location_operator'
        db.create_table('directory_location_operator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'])),
            ('operator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Operator'])),
        ))
        db.send_create_signal('directory', ['Location_operator'])

        # Adding model 'Location_hour'
        db.create_table('directory_location_hour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'])),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('hopen', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('hclose', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('directory', ['Location_hour'])

        # Adding model 'Service'
        db.create_table('directory_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('directory', ['Service'])

        # Adding model 'Location_service'
        db.create_table('directory_location_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Service'])),
        ))
        db.send_create_signal('directory', ['Location_service'])

        # Adding model 'Perspective'
        db.create_table('directory_perspective', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10)),
            ('heading', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10)),
            ('pitch', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10)),
            ('zoom', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=10)),
        ))
        db.send_create_signal('directory', ['Perspective'])

        # Adding model 'Report'
        db.create_table('directory_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'])),
            ('datecreated', self.gf('django.db.models.fields.DateField')()),
            ('dateofvisit', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('directory', ['Report'])

        # Adding model 'Project'
        db.create_table('directory_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('directory', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Interest'
        db.delete_table('directory_interest')

        # Deleting model 'Location'
        db.delete_table('directory_location')

        # Deleting model 'Operator'
        db.delete_table('directory_operator')

        # Deleting model 'Location_operator'
        db.delete_table('directory_location_operator')

        # Deleting model 'Location_hour'
        db.delete_table('directory_location_hour')

        # Deleting model 'Service'
        db.delete_table('directory_service')

        # Deleting model 'Location_service'
        db.delete_table('directory_location_service')

        # Deleting model 'Perspective'
        db.delete_table('directory_perspective')

        # Deleting model 'Report'
        db.delete_table('directory_report')

        # Deleting model 'Project'
        db.delete_table('directory_project')


    models = {
        'directory.interest': {
            'Meta': {'object_name': 'Interest'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'googleaddress': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Interest']", 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '10', 'blank': 'True'}),
            'mod_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 5, 0, 0)', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
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