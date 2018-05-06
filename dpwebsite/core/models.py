# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    USER_ID = models.CharField(max_length=50)
    USER_Name = models.CharField(max_length=50)
    USER_Password = models.CharField(max_length=50)
    USER_Email = models.CharField(max_length=50)
    USER_Address = models.CharField(max_length=100)
    USER_City = models.CharField(max_length=30)
    USER_Zip = models.IntegerField()
    USER_State = models.CharField(max_length=2)
    USER_FirstName = models.CharField(max_length=50)
    USER_LastName = models.CharField(max_length=50)
    USER_Degree = models.CharField(max_length=25)


class Courses(models.Model):
    CRSE_ID = models.CharField(max_length=15)
    CRSE_TITLE = models.CharField(max_length=25)
    DESCRIPTION = models.CharField(max_length=250)
    CRSE_SUBJECT = models.CharField(max_length=50)
    PREREQUISITE = models.CharField(max_length=250)


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
