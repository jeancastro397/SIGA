from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistroForm

def registro(request):
    if request.method == 'GET':
        context = {'form': RegistroForm()}
        return render(request, 'users/registro.html', context)
    
    if request.method == 'POST':
        form = RegistroForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        context = {'form': form}
        return render(request, 'users/registro.html', context)




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio u otra página
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'users/inicio_sesion.html', {'form': form})

