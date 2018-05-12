# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Users.objects.create(user=instance)
#    instance.profile.save()
##############################

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=50)
    userFirstName = models.CharField(max_length=50)
    userLastName = models.CharField(max_length=50)
    userDegree = models.CharField(max_length=25)
    userDesiredClasses = models.IntegerField()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)
    instance.profile.save()


class Courses(models.Model):
    courseID = models.CharField(max_length=15)
    courseTitle = models.CharField(max_length=25)
    courseDescription = models.CharField(max_length=250)
    courseSubject = models.CharField(max_length=50)
    courseLevel = models.IntegerField()


class PreRequisites(models.Model):
    preReqID = models.ForeignKey(Courses, related_name='prereq_id', on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, related_name='prereq_course_id', on_delete=models.CASCADE)


class Path(models.Model):
    userID = models.ForeignKey(Users, related_name='path_userID', on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, related_name='path_courseID', on_delete=models.CASCADE)
    pathQuarter = models.IntegerField()
    pathSteps = models.IntegerField()


class Availability(models.Model):
    courseID = models.ForeignKey(Courses, related_name='avail_courseID', on_delete=models.CASCADE)
    availQuarter = models.IntegerField()
    availDelivery = models.IntegerField()
