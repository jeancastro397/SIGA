from django.shortcuts import render


def registro(request):
    return render(request, 'user/templates/registro.html')
