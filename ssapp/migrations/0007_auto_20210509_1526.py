# Generated by Django 3.2 on 2021-05-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0006_auto_20210509_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='enrolled_course',
        ),
        migrations.AddField(
            model_name='account',
            name='enrolled_class',
            field=models.ManyToManyField(to='ssapp.ClassSchedule'),
        ),
    ]