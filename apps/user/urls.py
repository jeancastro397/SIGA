from django.urls import path
from .views import (
    login,
    registro
)


urlpatterns = [
    path('registrar/', registro, name='registrar' ),
    path('login/', login, name='login'),
]