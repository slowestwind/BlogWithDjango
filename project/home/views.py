from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	# return HttpResponse("home page ")
	return render(request, 'home/index.html')

def contact(request):
	# return HttpResponse("contact page ")
	return render(request, 'home/contact.html')

def about(request):
	# return HttpResponse("about page ")
	return render(request, 'home/about.html')