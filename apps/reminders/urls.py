from django.urls import path
from .views import crear_recordatorio, listarRecordatorio


urlpatterns = [
    path('crear-recordatorio/', crear_recordatorio, name='crear-recordatorio'),
    path('listar-recordatorio/', listarRecordatorio, name='listar-recordatorio'),
]