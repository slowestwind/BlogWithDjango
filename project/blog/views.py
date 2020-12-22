from django.shortcuts import render, HttpResponse
from blog.models import BlogPost
# import paginator to paginate our page
from django.core.paginator import Paginator

# Create your views here.

def home(request):
	# get all post
	allPost = BlogPost.objects.all()
	# paginator will show 3 posts per page
	paginator = Paginator(allPost, 3)
		# get the page number 
	page_number = request.GET.get('page')
		# show the page to user
	page_obj = paginator.get_page(page_number)
	context = {
		'allPost' : allPost,
		'page_obj':page_obj
	}
	return render(request, 'blog/blog.html', context)

def blog_post(request, slug):
	# return HttpResponse(f"Blog Slug is: {slug}")
	post = BlogPost.objects.filter(blog_slug=slug).first()

	post_param = {
		'post':post,
	}
	

	return render(request, 'blog/blogpost.html', post_param)
