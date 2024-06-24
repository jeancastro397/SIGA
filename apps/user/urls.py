from django.urls import path
from .views import (
    login_view,
    registro_view,
    perfil
)


urlpatterns = [
    path('registrar/', registro_view, name='registrar' ),
    path('login/', login_view, name='login'),
    path('perfil/', perfil, name='perfil'),
]