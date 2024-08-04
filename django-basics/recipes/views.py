from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def home(request : HttpRequest):
    return HttpResponse("Home")

def about(request : HttpRequest):
    return HttpResponse("about")

def contact(request : HttpRequest):
    return HttpResponse("contact")
