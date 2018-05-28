from django.conf.urls import url, include	
from django.contrib import admin
from django.contrib.staticfiles.urls import *
from . import views
from django.conf.urls.static import *
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]

