from __future__ import unicode_literals

from django.db import models


class Friends(models.Model):
    steamid1 = models.CharField(primary_key=True, max_length=64)
    steamid2 = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'friends'
        unique_together = (('steamid1', 'steamid2'),)


class ToCollect(models.Model):
    steamid = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'to_collect'


class UserGames(models.Model):
    steamid = models.CharField(primary_key=True, max_length=64)
    appid = models.CharField(max_length=32)
    timeplayed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_games'
        unique_together = (('steamid', 'appid'),)


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    persona_name = models.CharField(max_length=256, blank=True, null=True)
    real_name = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
