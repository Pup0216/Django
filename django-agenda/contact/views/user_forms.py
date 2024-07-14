from django.shortcuts import render,redirect
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Usuário Registrado")
            return redirect("contact:index")
        print("Form invalido")

    
    return render(
        request,
        'contact/register.html',
        {
            'form' : form
        }
    )
