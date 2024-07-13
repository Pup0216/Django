from django.shortcuts import render,redirect
from django.urls import reverse
from publication.forms import PublicationForm
from publication.models import Publication
# Create your views here.

def home(request):
    publications = Publication.objects.all()
    context = {
        'publications' : publications
    }
    return render(request,'publication/home.html',context)

def create(request):

    if request.POST:
        print(request.POST)
        form = PublicationForm(request.POST)
        if form.is_valid():
            print("Form valid")
            form.save()

            return redirect('publication:home')


    form_action = reverse('publication:create')

    context = {
        'content' : 'test',
        'form' : PublicationForm(),
        'form_action' : form_action
    }
    return render(request, 'publication/create.html',context)
