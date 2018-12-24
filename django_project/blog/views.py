from django.shortcuts import render
from django.http import HttpResponse

def home(request):#this function returns a line of html code for a browser
    return HttpResponse('<h1>Blog Home</h1>') #html for a browser to read

# Create your views here.
