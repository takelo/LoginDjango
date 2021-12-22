from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from mainapp.forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    # users = users.objects.get(public=slug);
    users = User.objects.all();

    return render (request, 'mainapp/index.html', {
        'title': 'Inicio',
        'users': users
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():

            register_form.save()
            messages.success(request, 'Registro exitoso, ingresa con tus credenciales')

            return redirect('login')

    return render (request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.warning(request, 'Usuario o Password invalidos!')
    return render (request, 'users/login.html', {
        'title': 'Login'
    })


def logout_user(request):

    logout(request)
    return redirect('login')



    