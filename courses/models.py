# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    dateCreated = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255)
    descript = models.TextField()

    def __str__(self):
        return self.title
        
