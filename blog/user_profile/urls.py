from django.conf.urls import url, include	
from django.contrib import admin
from django.contrib.staticfiles.urls import *
from . import views
from django.conf.urls.static import *
from django.conf import settings

app_name = 'user_profile'

urlpatterns = [
    url(r'^aboutme/$', views.aboutme, name="aboutme"),
    url(r'^aboutme/show', views.add_aboutme, name="add_aboutme"),
]
