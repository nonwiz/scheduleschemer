# Generated by Django 3.2 on 2021-05-09 03:46

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0003_auto_20210509_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='completed_course',
            field=picklefield.fields.PickledObjectField(default={'': ''}, editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='enrolled_course',
            field=picklefield.fields.PickledObjectField(default={'': ''}, editable=False),
        ),
        migrations.AlterField(
            model_name='class',
            name='daytime',
            field=picklefield.fields.PickledObjectField(default={'': ''}, editable=False),
        ),
        migrations.AlterField(
            model_name='classschedule',
            name='daytime',
            field=picklefield.fields.PickledObjectField(default={'': ''}, editable=False),
        ),
    ]
