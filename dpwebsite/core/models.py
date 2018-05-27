# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.decorators import login_required
from django.db import transaction

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

class ProfileManager(models.Manager):
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#    userEmail = models.CharField(max_length=50)

    #userID = models.CharField(max_length=50)
#    userName = models.CharField(max_length=50)
#    userPassword = models.CharField(max_length=50)
#
#    userFirstName = models.CharField(max_length=50, default='')
#    userLastName = models.CharField(max_length=50, default='')
#    courses_taken = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_user_profile, sender=User)


class Users(models.Model):

    userID = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=50)
#    userFirstName = models.CharField(max_length=50)
#    userLastName = models.CharField(max_length=50)



class Courses(models.Model):
    CRSE_ID = models.IntegerField()
    CRSE_TITLE = models.TextField()
    CRSE_DESCRIPTION = models.TextField()
    CRSE_SUBJECT = models.CharField(max_length=50)
    CRSE_PREREQUISITE = models.TextField()
    CRSE_NBR = models.IntegerField()


class PreRequisites(models.Model):
    PREREQUISITE_ID = models.ForeignKey(Courses, related_name='prereq_id', on_delete=models.CASCADE)
    CRSE_ID = models.ForeignKey(Courses, related_name='prereq_course_id', on_delete=models.CASCADE)


class Path(models.Model):
    USER_ID = models.ForeignKey(Users, related_name='path_userID', on_delete=models.CASCADE)
    courseID = models.ForeignKey(Courses, related_name='path_courseID', on_delete=models.CASCADE)
    pathQuarter = models.IntegerField()
    pathSteps = models.IntegerField()


class Availability(models.Model):
    CRSE_ID = models.ForeignKey(Courses, related_name='avail_CRSE_ID', on_delete=models.CASCADE)
    availQuarter = models.CharField(max_length=10)
    availDelivery = models.CharField(max_length=10)
