from django.shortcuts import render, get_object_or_404, redirect
from .models import Recordatorio
from .forms import RecordatorioForm



def crear_recordatorio(request):
    if request.method == 'GET':
        context = {
            "title": "Crear Recordatorio",
            "recordatorioForm": RecordatorioForm()  # Corregido el nombre aquí
        }
        return render(request, "reminders/crear-recordatorio.html", context)

    if request.method == 'POST':
        recordatorioForm = RecordatorioForm(data=request.POST)  # Corregido el nombre aquí
        if recordatorioForm.is_valid():
            recordatorioForm.save()
            return redirect("home")

        context = {
            "title": "Crear Recordatorio",
            "recordatorioForm": recordatorioForm  # Corregido el nombre aquí
        }
        return render(request, "reminders/crear-recordatorio.html", context)


def listar_recordatorio(request):
    recordatorios = Recordatorio.objects.all()
    context = {
        'title': 'Listar Recordatorios',
        'recordatorios': recordatorios
    }
    return render(request, 'reminders/listar-recordatorio.html', context)


def modificar_recordatorio(request, pk):
    recordatorio = get_object_or_404(Recordatorio, pk=pk)

    if request.method == 'POST':
        form = RecordatorioForm(request.POST, instance=recordatorio)
        if form.is_valid():
            form.save()
            return redirect('home')  # Cambia 'home' por la URL a la que quieres redirigir después de modificar
    else:
        form = RecordatorioForm(instance=recordatorio)

    context = {
        'title': 'Modificar Recordatorio',
        'form': form,
        'recordatorio': recordatorio,
    }
    return render(request, 'reminders/modificar-recordatorio.html', context)
