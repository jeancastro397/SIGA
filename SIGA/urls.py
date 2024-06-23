from django.contrib import admin
from django.urls import path, include
from .views import index
from apps.notes.urls import urlspatterns as notas
from apps.reminders.urls import urlpatterns as recordatorios


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", index, name="home"),
    path("usuarios/", include('apps.user.urls')),
    path("notas/", include(notas)),
    path("recordatorios/", include(recordatorios))
]
