from django.contrib import admin
from django.urls import path, include
from apps.notes.urls import urlspatterns as notas


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('apps.user.urls')),
    path("notas/", include(notas)),
]
