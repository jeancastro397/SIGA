from django.urls import path
from .views import crearRecordatorio, listarRecordatorio, eliminarRecordatorio

urlpatterns = [
    path('crear-recordatorio/', crearRecordatorio, name='crear-recordatorio'),
    path('listar-recordatorios/', listarRecordatorio, name='listar-recordatorios'),
    path('eliminar-recordatorio/<int:pk>', eliminarRecordatorio, name='eliminar-recordatorio'),
]
