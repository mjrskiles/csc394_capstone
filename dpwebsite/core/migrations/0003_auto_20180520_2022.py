# Generated by Django 2.0.4 on 2018-05-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180520_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='CRSE_NBR',
            field=models.IntegerField(),
        ),
    ]
