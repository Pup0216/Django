from typing import Any
from django.shortcuts import render

#forms
from contact.forms import ContactForm


# Create your views here.

def create(request):
    if request.POST:
        context = {
            'form': ContactForm(request.POST)
        }
        print("Dados recebidos")
        return render(request,'contact/create.html',context)
    context = {
        'form': ContactForm()
    }
    return render(request,'contact/create.html',context)


  
    
