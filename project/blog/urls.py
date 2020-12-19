
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="blog_home"),
	path('<slug:slug>', views.blog_post, name='blogpost'),
]