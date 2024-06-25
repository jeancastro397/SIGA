from django.urls import path
from .views import crearNota, listarNota, modificarNota


urlspatterns = [
    path('crear-nota/', crearNota, name='crear-nota'),
    path('listar-notas/', listarNota, name='listar-notas'),
    path('modificar-notas/<int:pk>', modificarNota, name='modificar-notas'),
]