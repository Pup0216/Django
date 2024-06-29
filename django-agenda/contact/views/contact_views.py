from django.shortcuts import render
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show = True).order_by('id')[0:10]
    context = {
        'contacts' : contacts
    }
    #print(contacts.query)
    return render(request,'contact/index.html',context)

def contact(request, id):
    contact = Contact.objects.filter(pk = id).first()
    if contact is None:
        #retornar uma pagina 404 
        raise Http404
    
    
    context = { 
        'contact' : contact
    }
    return render(request,'contact/contact.html',context)