from django.urls import path
from .views import login_view, registro_view, perfil, cerrar_sesion


urlpatterns = [
    path("registrar/", registro_view, name="registrar"),
    path("login/", login_view, name="login"),
    path("logout/", cerrar_sesion, name="logout"),
    path("perfil/", perfil, name="perfil"),
]
