# Generated by Django 3.2 on 2021-05-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0007_account_earned_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ManyToManyField(blank=True, related_name='courses', to='ssapp.Faculty'),
        ),
    ]