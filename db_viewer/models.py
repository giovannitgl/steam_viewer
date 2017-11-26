# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class App(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    devid = models.ForeignKey('Developer', models.DO_NOTHING, db_column='devid', blank=True, null=True,related_name='dev')
    pubid = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='pubid', blank=True, null=True,related_name='publishid')
    metascore = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'App'


class Apptag(models.Model):
    appid = models.ForeignKey(App, models.DO_NOTHING, db_column='appid', blank=True, null=True)
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tagid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppTag'


class Developer(models.Model):
    devid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Developer'



class Friendship(models.Model):
    uid1 = models.ForeignKey('User', models.DO_NOTHING, db_column='uid1', primary_key=True,related_name='fid1')
    uid2 = models.ForeignKey('User', models.DO_NOTHING, db_column='uid2',related_name='fid2')

    class Meta:
        managed = False
        db_table = 'Friendship'
        unique_together = (('uid1', 'uid2'),)


class Publisher(models.Model):
    pubid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Publisher'


class Relatedapps(models.Model):
    appid = models.ForeignKey(App, models.DO_NOTHING, db_column='appid', primary_key=True,related_name='realted_appid_owner')
    relatedid = models.ForeignKey(App, models.DO_NOTHING, db_column='relatedid',related_name='related_id')

    class Meta:
        managed = False
        db_table = 'RelatedApps'
        unique_together = (('appid', 'relatedid'),)


class Review(models.Model):
    appid = models.ForeignKey(App, models.DO_NOTHING, db_column='appid', primary_key=True)
    positive = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Review'


class Tag(models.Model):
    tagid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tag'


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=64)
    nickname = models.CharField(max_length=256, blank=True, null=True)
    realname = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Userapps(models.Model):
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='uid', primary_key=True)
    appid = models.ForeignKey(App, models.DO_NOTHING, db_column='appid')
    timeplayed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserApps'
        unique_together = (('uid', 'appid'),)
