from django.urls import path
from .views import (
    index,
    login,
    registro
)


urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro' ),
    path('login/', login, name='login'),
]