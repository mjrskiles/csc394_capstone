# Generated by Django 2.0.4 on 2018-05-06 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availQuarter', models.IntegerField()),
                ('availDelivery', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(max_length=15)),
                ('courseTitle', models.CharField(max_length=25)),
                ('courseDescription', models.CharField(max_length=250)),
                ('courseSubject', models.CharField(max_length=50)),
                ('courseLevel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathQuarter', models.IntegerField()),
                ('pathSteps', models.IntegerField()),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_courseID', to='core.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='PreRequisites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prereq_course_id', to='core.Courses')),
                ('preReqID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prereq_id', to='core.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=50)),
                ('userEmail', models.CharField(max_length=50)),
                ('userAddress', models.CharField(max_length=100)),
                ('userCity', models.CharField(max_length=30)),
                ('userZip', models.IntegerField()),
                ('userState', models.CharField(max_length=2)),
                ('userFirstName', models.CharField(max_length=50)),
                ('userLastName', models.CharField(max_length=50)),
                ('userDegree', models.CharField(max_length=25)),
                ('userDesiredClasses', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='path',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_userID', to='core.Users'),
        ),
        migrations.AddField(
            model_name='availability',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avail_courseID', to='core.Courses'),
        ),
    ]
