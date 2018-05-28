from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length = 100) 
	slug = models.SlugField()
	body = models.TextField(default='hello this is the article you have been waiting for.')
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	author = models.ForeignKey(User, default=None)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]