from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def home(request):
	return HttpResponse("blog home page ")

def blog_post(request, slug):
	return HttpResponse(f"Blog Slug is: {slug}")
