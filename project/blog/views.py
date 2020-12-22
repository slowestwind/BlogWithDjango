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
	print("pagenumber"+page_number)
		# show the page to user
	page_obj = paginator.get_page(page_number)
	
	# print("page obj"+page_obj)
	
	context = {
		'allPost' : allPost,
		'page_obj':page_obj
	}
	return render(request, 'blog/blog.html', context)

def blog_post(request, slug):
	# return HttpResponse(f"Blog Slug is: {slug}")
	post = BlogPost.objects.filter(blog_slug=slug).first()
	# get current post id 
	# if it is > 0 
	# get the current post id
	currentId = post.blog_id
	# print(post.blog_id)
	nPost = ''
	pPost = ''
	if post.blog_id == 1:
		# get the next post
		nextId = currentId+1
		nPost = BlogPost.objects.filter(blog_id=nextId).first()
		# nPost = "hello there if first post"
		print(nPost)

	else:
		prevId = currentId-1
		pPost = BlogPost.objects.filter(blog_id=prevId).first()
		# pPost = "if post greater than 1 and previous section"
		print(pPost)
			# get the next post
		nextId = currentId+1
		nPost = BlogPost.objects.filter(blog_id=nextId).first()
		# pPost = "if post greater than 1 and next section"
		print(nPost)
			
	post_param = {
		'post' : post,
		'pPost' : pPost,
		'nPost' : nPost,
	}
	

	return render(request, 'blog/blogpost.html', post_param)
