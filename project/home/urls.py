from django.contrib import admin
from django.urls import path, include 
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('', views.home, name="home"),
	path('contact/', views.contact, name="contact"),
	path('about/', views.about, name="about"),	
	path('search/', views.search, name="search"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
