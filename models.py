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
    devid = models.ForeignKey('Developer', models.DO_NOTHING, db_column='devid', blank=True, null=True)
    pubid = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='pubid', blank=True, null=True)
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
    uid1 = models.ForeignKey('User', models.DO_NOTHING, db_column='uid1', primary_key=True)
    uid2 = models.ForeignKey('User', models.DO_NOTHING, db_column='uid2')

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
    appid = models.ForeignKey(App, models.DO_NOTHING, db_column='appid', primary_key=True)
    relatedid = models.ForeignKey(App, models.DO_NOTHING, db_column='relatedid')

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
