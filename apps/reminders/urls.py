from django.urls import path
from .views import crear_recordatorio


urlpatterns = [
    path('crear-recordatorio/', crear_recordatorio, name='crear-recordatorio'),
]