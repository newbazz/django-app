# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='date_of_birth',
        ),
    ]