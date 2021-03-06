from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from .forms import UserCreationFormCustom


def welcome(request):
    # Verificamos si el usuario está autenticado
    if request.user.is_authenticated:
        # Retornamos la página si está logeado
        return render(request, "core/welcome.html")
    # si no está logeado, redirecciona al login
    return redirect('/login')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "authentication/login.html", {'form': form})


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationFormCustom()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationFormCustom(data=request.POST)
        # Si el formulario es válido
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "authentication/register.html", {'form': form})


def logout(request):
    # Hacemos el logout con esta función
    do_logout(request)
    # Redirigimos
    return redirect('/')
