from django.urls import path
from .views import crearNota


urlspatterns = [
    path('crear-nota/', crearNota, name='crear-nota'),
]