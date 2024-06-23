from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistroForm, PerfilForm, PasswordUpdateForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')  # Redirige a la página principal u otra página deseada
    else:
        form = RegistroForm()
    return render(request, 'users/registro.html', {'form': form})



## Formulario Login
def login(request):
    # Entrega un formulario limpio al entrar a la página
    if request.method == 'GET':
        context = {
            "title": "Iniciar sesión",
            "loginForm": LoginForm()
        }
        return render (request, "users/login.html", context)

    # Valida el formulario, sino es válido, devuelve el formulario con los campos rellenados
    if request.method == 'POST':
        loginForm = LoginForm(data=request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            valid_user = authenticate(request, username=username, password=password)
            if valid_user is not None:
                login(request, valid_user)
                return redirect("home")  # Redirige a la página de inicio u otra página
            else:
                loginForm.add_error(None, 'Nombre de usuario o contraseña incorrectos')
        context = {
            "title": "Iniciar sesión",
            "loginForm": loginForm
        }
        return render(request, "users/login.html", context)



# Formulario de editar perfil de usuario
@login_required
def perfil(request):
    if request.method == 'POST:':
        userForm = PerfilForm(request.POST, instance=request.user)
        passwordForm = PasswordUpdateForm(user=request.user, data=request.POST)
        if userForm.is_valid() and passwordForm.is_valid():
            userForm.save()
            user = passwordForm.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Tu perfil se ha actualizado correctamente.")
            return redirect('perfil')
    
    else:
        userForm = PerfilForm(instance=request.user)
        passwordForm = PasswordUpdateForm(user=request.user)
    
    return render(request, 'users/perfil.html', {
        'userForm': userForm,
        'passwordForm': passwordForm
    })