# Generated by Django 3.2 on 2021-04-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]