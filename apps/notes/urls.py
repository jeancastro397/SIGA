from django.urls import path
from .views import crearNota, listarNota, modificarNota, eliminarNota


urlspatterns = [
    path('crear-nota/', crearNota, name='crear-nota'),
    path('listar-notas/', listarNota, name='listar-notas'),
    path('modificar-notas/<int:pk>', modificarNota, name='modificar-notas'),
    path('eliminar-nota/<int:pk>', eliminarNota, name='eliminar-nota'),
]