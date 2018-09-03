# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group_id = models.IntegerField

    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreAvailability(models.Model):
    availquarter = models.CharField(db_column='availQuarter', max_length=10)  # Field name made lowercase.
    availdelivery = models.CharField(db_column='availDelivery', max_length=10)  # Field name made lowercase.
    crse_id = models.ForeignKey('CoreCourses', models.DO_NOTHING, db_column='CRSE_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_availability'


class CoreCourses(models.Model):
    id = models.IntegerField
    CRSE_ID = models.IntegerField(db_column='CRSE_ID')  # Field name made lowercase.
    CRSE_TITLE = models.TextField(db_column='CRSE_TITLE')  # Field name made lowercase.
    CRSE_DESCRIPTION = models.TextField(db_column='CRSE_DESCRIPTION')  # Field name made lowercase.
    CRSE_SUBJECT = models.CharField(db_column='CRSE_SUBJECT', max_length=50)  # Field name made lowercase.
    CRSE_PREREQUISITE = models.TextField(db_column='CRSE_PREREQUISITE')  # Field name made lowercase.
    CRSE_NBR = models.IntegerField(db_column='CRSE_NBR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_courses'


class CorePath(models.Model):
    pathquarter = models.IntegerField(db_column='pathQuarter')  # Field name made lowercase.
    pathsteps = models.IntegerField(db_column='pathSteps')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID_id')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='courseID_id')  # Field name made lowercase.
    path_id = models.CharField(db_column="path_id",max_length=20)

    class Meta:
        managed = False
        db_table = 'core_path'


class CorePrerequisites(models.Model):
    crse_id = models.ForeignKey(CoreCourses, models.DO_NOTHING, db_column='CRSE_ID_id',related_name= 'CorePreCourseID')  # Field name made lowercase.
    prerequisite_id = models.ForeignKey(CoreCourses, models.DO_NOTHING, db_column='PREREQUISITE_ID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_prerequisites'


class CoreProfile(models.Model):
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.
    userfirstname = models.CharField(db_column='userFirstName', max_length=50)  # Field name made lowercase.
    userlastname = models.CharField(db_column='userLastName', max_length=50)  # Field name made lowercase.
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'core_profile'


class CoreUsers(models.Model):
    userid = models.CharField(db_column='userID', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=50)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_users'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
