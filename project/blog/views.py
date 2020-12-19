from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def home(request):
	# return HttpResponse("blog home page ")
	return render(request, 'blog/blog.html')

def blog_post(request, slug):
	# return HttpResponse(f"Blog Slug is: {slug}")
	slug = slug
	param = {"slug":"slug"}
	return render(request, 'blog/blogpost.html', param)
