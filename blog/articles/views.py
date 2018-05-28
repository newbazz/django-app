# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import *
from django.http import *
from django.contrib.auth.decorators import login_required

def article_list(request):
	article = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html',{'articles':article})

def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_details.html',{'articles':article})

@login_required(login_url='/accounts/login/')
def article_create(request):
	return render(request, 'articles/article_create.html')
