from __future__ import unicode_literals
from . import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

@login_required(login_url='/accounts/login/')
def aboutme(request):
	form = forms.User_Profile()
	return render(request, 'user_profile/aboutme.html',{'form':form})

@login_required(login_url='/accounts/login/')
def add_aboutme(request):
	form = forms.User_Profile(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.name = request.user
		instance.save()
		return HttpResponse('<h1>Saved Successfully</h1>')
	else:
		return redirect('user_profile:aboutme')

