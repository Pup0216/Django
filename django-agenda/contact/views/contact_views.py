from django.shortcuts import render,redirect
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator



# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show = True).order_by('id')
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj,
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

    contacts = Contact.objects.filter(show = True)\
    .filter(name__icontains=value)\
    .order_by('-id')

    #lookup

    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'title' : 'Agenda',
    }
    return render(request,'contact/index.html',context)



