from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import BlogPost

# Create your views here.
def home(request):
	allPost = BlogPost.objects.all()
	context = {
		'allPost':allPost,
	}
	print(context)
	return render(request, 'home/index.html', context)

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

def about(request):
	return render(request, 'home/about.html')