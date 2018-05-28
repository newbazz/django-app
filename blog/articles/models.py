from __future__ import unicode_literals
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length = 100) 
	slug = models.SlugField()
	body = models.TextField(default='hello this is the article you have been waiting for.')
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	# add in author later

	# add in thumbnail later

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]