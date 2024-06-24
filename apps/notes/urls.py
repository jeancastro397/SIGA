from django.urls import path
from .views import crearNota, listarNota


urlspatterns = [
    path('crear-nota/', crearNota, name='crear-nota'),
    path('listar-notas/', listarNota, name='listar-notas'),
]