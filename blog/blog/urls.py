from django.conf.urls import url, include	
from django.contrib import admin
from django.contrib.staticfiles.urls import *
from . import views
from django.conf.urls.static import *
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about),
    url(r'^$', views.home),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
