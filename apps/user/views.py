from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistroForm, PerfilForm, PasswordUpdateForm
from sweetify import success, warning


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success(
                request,
                "Registrado correctamente",
                text="Ahora puede usar la página libremente",
                timer=3000,
                button="OK",
            )
            return redirect(
                "login"
            )  # Redirige a la página principal u otra página deseada
        else:
            warning(
                request,
                "Ups...",
                text="Observe el formulario y valide sus datos",
                button="OK",
            )
    else:
        form = RegistroForm()
    return render(request, "users/registro.html", {"form": form})


## Formulario Login
def login_view(request):
    # Entrega un formulario limpio al entrar a la página
    if request.method == "GET":
        context = {"title": "Iniciar sesión", "loginForm": LoginForm()}
        return render(request, "users/login.html", context)

    # Valida el formulario, sino es válido, devuelve el formulario con los campos rellenados
    if request.method == "POST":
        loginForm = LoginForm(data=request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data["username"]
            password = loginForm.cleaned_data["password"]
            valid_user = authenticate(request, username=username, password=password)
            if valid_user is not None:
                login(request, valid_user)
                success(
                    request,
                    "Inicio de sesión exitoso!!",
                    timer=3000,
                    button="OK",
                )
                return redirect("home")  # Redirige a la página de inicio u otra página
            else:
                loginForm.add_error(None, "Nombre de usuario o contraseña incorrectos")
                warning(
                    request,
                    "Ingrese credenciales válidas",
                    timer=3000,
                    button="OK",
                )
        context = {"title": "Iniciar sesión", "loginForm": loginForm}
        return render(request, "users/login.html", context)


# Formulario de editar perfil de usuario
@login_required
def perfil(request):
    if request.method == "POST":
        user_form = PerfilForm(request.POST, instance=request.user)
        password_form = PasswordUpdateForm(user=request.user, data=request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(
                request, password_form.user
            )  # Actualizar la sesión con la nueva contraseña
            success(
                request,
                "Actualización exitosa!!",
                text="Tu perfil y contraseña han sido actualizados exitosamente.",
                timer=3000,
                button="OK",
            )
            return redirect("perfil")
        elif user_form.is_valid():
            user_form.save()
            success(
                request,
                "Actualización exitosa!!",
                text="Tu perfil ha sido actualizado exitosamente.",
                timer=3000,
                button="OK",
            )
            return redirect("perfil")
        elif password_form.is_valid():
            password_form.save()
            update_session_auth_hash(
                request, password_form.user
            )  # Actualizar la sesión con la nueva contraseña
            messages.success(request, "Tu contraseña ha sido actualizada exitosamente.")
            success(
                request,
                "Contraseña cambiada!!",
                text="Tu contraseña ha sido actualizada exitosamente.",
                timer=3000,
                button="OK",
            )
            return redirect("perfil")
        else:
            warning(
                request,
                "Perfil no actualizado",
                text="Revice bien los campos e intenténtelo nuevamente.",
                timer=5000,
                button="OK",
            )
    else:
        user_form = PerfilForm(instance=request.user)
        password_form = PasswordUpdateForm(user=request.user)

    return render(
        request,
        "users/perfil.html",
        {
            "user_form": user_form,
            "password_form": password_form,
        },
    )


@login_required
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario

    # Eliminar la cookie de sesión
    if request.session.session_key:
        request.session.delete(request.session.session_key)

    # Eliminar otras cookies si es necesario (por ejemplo, si tienes cookies personalizadas)

    # Redirige a alguna página después de cerrar sesión
    return render(request, "users/logout.html")


@login_required
def eliminar_cuenta_view(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        if request.session.session_key:
            request.session.delete(request.session.session_key)
        user.delete()
        success(
            request,
            "Cuenta eliminada",
            text="Tu cuenta ha sido eliminada correctamente.",
            timer=3000,
            button="OK",
        )
        return redirect("home")
    return redirect("perfil")
