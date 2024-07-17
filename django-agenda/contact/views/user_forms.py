from django.shortcuts import render,redirect
from contact.forms import RegisterForm, UpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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

def userLogin(request):
    form = AuthenticationForm(request)

    if request.POST:
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            messages.success(request,"Logado com sucesso")
            return redirect('contact:index')
        
        messages.error(request,'Login invalido')
    context = {
        'form' : form,
        'title' : 'Register'
    }
    return render(request,'contact/login.html',context)


@login_required(login_url='contact:login') #caso o usuario não estja logado
def userLogout(request):
    auth.logout(request)
    return redirect('contact:login')



#Normalmente não permitir o usuario atualizar o email e o user
@login_required(login_url='contact:login') #caso o usuario não estja logado
def userUpdate(request):
    form = UpdateForm(instance=request.user)

    if request.POST:
        form = UpdateForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Dados atualizados")
            return redirect('contact:index')
    context = {
        'form' : form,
        'title' : "Update"
    }
    return render(
        request,
        'contact/register.html',
        context
    )