from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Función para iniciar sesión
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'accounts/login.html')

# Función para cerrar sesión
def user_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('home')

# Función para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "El correo ya está registrado.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
                return redirect('login')
        else:
            messages.error(request, "Las contraseñas no coinciden.")
    
    return render(request, 'accounts/register.html')
