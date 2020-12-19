from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("home page ")

def contact(request):
	return HttpResponse("contact page ")

def about(request):
	return HttpResponse("about page ")
