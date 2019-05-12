# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    git = models.URLField(max_length=300)
    heroku = models.URLField(max_length=300)

    def __str__(self):
        return self.title

    def save_projects(self):
        self.save()

    def delete_projects(self):
        self.delete()

