from django.urls import path
from .views import crearRecordatorio, listarRecordatorio

urlpatterns = [
    path('crear-recordatorio/', crearRecordatorio, name='crear-recordatorio'),
    path('listar-recordatorios/', listarRecordatorio, name='listar-recordatorios'),
]
