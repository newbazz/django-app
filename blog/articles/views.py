# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import *

def article_list(request):
	article = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html',{'articles':article})