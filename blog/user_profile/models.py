from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

class User_Profile(models.Model):
	name = models.ForeignKey(User, default=None)
	sex = models.TextField(default='male')
	body = models.TextField(default='I am a blogger.')
	# add date of birth as a parameter
