# urls.py
from django.urls import path
from .views import crear_recordatorio, listar_recordatorio,modificar_recordatorio  # Importa la vista listar_recordatorio

urlpatterns = [
    path('crear-recordatorio/', crear_recordatorio, name='crear-recordatorio'),
    path('listar-recordatorio/', listar_recordatorio, name='listar-recordatorio'),
    path('modificar-recordatorio/<int:pk>/', modificar_recordatorio, name='modificar-recordatorio'), 
    
]
