# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField()
    description = models.CharField()

