from django.shortcuts import render


##  VISTA PRINCIPAL DE LA PÁGINA
def index(request):
    context = {
        "title": "Bienvenido a su recordatorio de notas",
        "subtitle": "Para usar la página, puede registrarse y usar todas las funciones"
    }
    return render(request, 'users/index.html', context)