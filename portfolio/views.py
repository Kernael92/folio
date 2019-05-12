# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
 

# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request, projects_id):
    project = get_object_or_404(Projects, pk=projects_id)
    return render(request, 'portfolio/projects.html', {'project': project})
