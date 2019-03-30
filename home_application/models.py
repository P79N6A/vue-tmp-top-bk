# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    when_created = models.CharField(max_length=50)
    when_modified = models.CharField(max_length=50)


class MyUser(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    time_created = models.CharField(max_length=50)


class HostInfo(models.Model):
    bk_host_innerip = models.CharField(max_length=50)
    bk_os_name = models.CharField(max_length=50)
    bk_host_name = models.CharField(max_length=50)
    bk_cloud_id = models.CharField(max_length=50)
    bk_biz_id = models.CharField(max_length=50)
    bk_host_id = models.CharField(max_length=50)
    bk_mem = models.CharField(max_length=50)
    bk_cpu = models.CharField(max_length=50)
    bk_disk = models.CharField(max_length=50)


class HostInfoMonitor(models.Model):
    bk_host_name = models.CharField(max_length=50)
    bk_host_innerip = models.CharField(max_length=50)
    bk_host_id = models.CharField(max_length=50)
    bk_biz_id = models.CharField(max_length=100)
    bk_cloud_id = models.CharField(max_length=50)
