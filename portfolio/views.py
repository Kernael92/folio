# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from .models import Projects
 

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    project_list = Projects.objects.all()
    return render(request, 'portfolio/projects.html', {'project': project_list})
