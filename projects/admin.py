# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description')



admin.site.register(Project, ProjectAdmin)
