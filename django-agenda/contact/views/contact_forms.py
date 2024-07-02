from django.shortcuts import render,redirect
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator



# Create your views here.

def create(request):
    if request.POST:
        print(request.POST.get("name"))
        print(request.POST.get("last_name"))
    context = {
 
    }
    return render(request,'contact/create.html',context)
