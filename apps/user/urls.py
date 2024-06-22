from django.urls import path
from .views import registro , login_view


urlpatterns = [
    path('', views.index_view, name='index'),
    path('registro/', registro, name='registro' ),
    path('login/', login_view, name='login'),
]