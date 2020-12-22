from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import BlogPost
# import paginator to paginate our page
from django.core.paginator import Paginator

# Create your views here.
# this functin will be executed if user visited on home link.
def home(request):
	allPost = BlogPost.objects.all()
	param = {
		'allPost':allPost
	}

	return render(request, 'home/index.html', param)

# this functin will be executed if user visited on contact link.
def contact(request):
	if(request.method == "POST"):
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		# if the contact form not filled properly
		if len(name)>3 and len(email)>3 and len(message)>3:
			contact = Contact(contact_name=name, contact_email=email, contact_message=message)
			contact.save()
			messages.success(request,"successfully submitted.")
		else:
			messages.error(request, "please fill this form properly!")


	return render(request, 'home/contact.html')

# this functin will be executed if user visited on about link.
def about(request):
	return render(request, 'home/about.html')


# this functin will be executed if user visited on search button in navbar.
def search(request):
	
	# get the query from search form
	query = request.GET['query']

	# validate the query
	if len(query) > 50:
		allPosts = []
	else: 		
	# search query in the title and description
		titleSearch = BlogPost.objects.filter(blog_title__icontains = query)
		contentSearch = BlogPost.objects.filter(blog_content__icontains = query)
		allPosts = titleSearch.union(contentSearch)
		messages.success(request, "Your search Result")
		# paginator will show 3 posts per page
		paginator = Paginator(allPosts, 3)
		# get the page number 
		page_number = request.GET.get('page')
		# show the page to user
		page_obj = paginator.get_page(page_number)
	# put it in the parameter to pass in search result
	param = {
		'allPosts':allPosts,
		'query':query,
		'page_obj':page_obj
	}
	return render(request, 'home/search.html', param)