# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_remove_user_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='sex',
            field=models.CharField(default='male', max_length=100),
        ),
    ]