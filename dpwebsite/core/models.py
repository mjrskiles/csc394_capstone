# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
    CRSE_ID = models.IntegerField(max_length=15)
    CRSE_TITLE = models.CharField(max_length=25)
    CRSE_DESCRIPTION = models.CharField(max_length=250)
    CRSE_SUBJECT = models.CharField(max_length=50)
    CRSE_PREREQUISITE = models.CharField(max_length=250)
    CRSE_NBR = models.CharField(max_length=3)


class PreRequisites(models.Model):
    PREREQUISITE_ID = models.ForeignKey(Courses, related_name='prereq_id', on_delete=models.CASCADE)
    CRSE_ID = models.ForeignKey(Courses, related_name='prereq_course_id', on_delete=models.CASCADE)


class Path(models.Model):
    USER_ID = models.ForeignKey(Users, related_name='path_userID', on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, related_name='path_courseID', on_delete=models.CASCADE)
    pathQuarter = models.IntegerField()
    pathSteps = models.IntegerField()


class Availability(models.Model):
    CRSE_ID = models.ForeignKey(Courses, related_name='avail_courseID', on_delete=models.CASCADE)
    availQuarter = models.IntegerField()
    availDelivery = models.IntegerField()
