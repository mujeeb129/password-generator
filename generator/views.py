from django.shortcuts import render
from django.http import HttpResponse
from .algorithems.generation import generate

# Create your views here.

def generator(request):
	return render(request , 'generator/index.html')

def password(request):

	password = generate(request)
	return render(request , 'generator/password.html' , {'passwords' : password })