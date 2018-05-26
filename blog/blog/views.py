from django .http import HttpResponse
from django.shortcuts import render

def about(request):
	return render(request, 'about.html')
	#return HttpResponse('<h3>Welcome to the blog</h3>')

def home(request):
	return render(request, 'homepage.html')
	#return HttpResponse('<h3>Welcome to the homepage</h3>')