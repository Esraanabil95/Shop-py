# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


