from django.shortcuts import render, HttpResponse
from blog.models import BlogPost

# Create your views here.

def home(request):
	allPost = BlogPost.objects.all()
	context = {
		'allPost' : allPost
	}
	return render(request, 'blog/blog.html', context)

def blog_post(request, slug):
	# return HttpResponse(f"Blog Slug is: {slug}")
	slug = slug
	param = {"slug":"slug"}
	return render(request, 'blog/blogpost.html', param)
