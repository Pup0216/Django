from django.shortcuts import render,redirect
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show = True).order_by('id')[0:10]
    context = {
        'contacts' : contacts,
        'title' : 'Agenda'
    }
    #print(contacts.query)
    return render(request,'contact/index.html',context)

def contact(request, id):
    contact = Contact.objects.filter(pk = id).first()
    if contact is None:
        #retornar uma pagina 404 
        raise Http404
    
    
    context = { 
        'contact' : contact,
        'title' : contact.name,
    }
    return render(request,'contact/contact.html',context)

def search(request):
    value = request.GET.get('q','').strip()
    #.strip() remove espaços vazios da string
    # q == name do form
    if value == '':
        print("Redirecionando...")
        return redirect('contact:index')

    print(value)
    contacts = Contact.objects.filter(show = True)\
    .filter(name__icontains=value)\
    .order_by('-id')

    #lookup


    context = {
        'contacts': contacts,
        'title' : 'Agenda',
    }
    return render(request,'contact/index.html',context)