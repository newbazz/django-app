# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
	article = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html',{'articles':article})

def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_details.html',{'articles':article})

@login_required(login_url='/accounts/login/')
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('article:list')

	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html', {'form': form})
