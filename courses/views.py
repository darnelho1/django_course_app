# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

# Create your views here.
def course_catalog(req):
    courses = Course.objects.all()
    output = ', '.join ([str(course) for course in courses])
    return HttpResponse(output)
