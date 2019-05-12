# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Projects

# Create your tests here.
class ProjectsTestClass(TestCase):
    
    def setUp(self):
        self.awards = Projects(title = 'awards', description = 'A web application to enable users to vote on different projects depending on usability and design.', image = 'image.jpg', git = 'https://github.com/Kernael92/folio', heroku = 'https://folio.heroku.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.awards, Projects))

    def test_save_method(self):
        self.awards.save_projects()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.awards.save_projects()
        projects = Projects.objects.all().delete()
        self.assertFalse(len(projects) == 0)
        