from django.urls import path
from .views import (
    login,
    registro,
    perfil
)


urlpatterns = [
    path('registrar/', registro, name='registrar' ),
    path('login/', login, name='login'),
    path('perfil/', perfil, name='perfil'),
]