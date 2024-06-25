from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReminderForm
from .models import Reminder
from apps.notes.models import Note
from sweetify import success, warning


@login_required
def crearRecordatorio(request):
    if request.method == 'GET':
        context = {
            "title": "Nuevo Recordatorio",
            "form": ReminderForm(),
            "notes": Note.objects.filter(user=request.user)  # Filtrar notas del usuario logueado
        }
        return render(request, "reminders/crear-recordatorio.html", context)

    if request.method == 'POST':
        form = ReminderForm(data=request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            success(
                request,
                "Recordatorio creado",
                text="El recordatorio ha sido creado con éxito",
                timer=4000,
                button="Listo",
            )
            return redirect("listar-recordatorios")
        
        else:
            warning(
            request,
            "Error al crear el recordatorio",
            text="Revise los campos e inténtelo nuevamente.",
            timer=3000,
            button="OK",
        )
        context = {
            "title": "Nuevo Recordatorio",
            "form": form,
            "notes": Note.objects.filter(user=request.user)  # Filtrar notas del usuario logueado
        }
        return render(request, "reminders/crear-recordatorio.html", context)



@login_required
def listarRecordatorio(request):
    if request.method == 'GET':
        context = {
            "title": "Lista de recordatorios",
            "listReminders": Reminder.objects.all()
        }
        return render(request, "reminders/listar-recordatorios.html", context)


@login_required
def eliminarRecordatorio(request, pk):
    recordatorio = get_object_or_404(Reminder, pk=pk, user=request.user)

    if request.method == 'POST':
        if recordatorio.pk == pk:
            recordatorio.delete()
            success(
                request,
                "Recordatorio eliminado con éxito.",
                timer=5000,
                button="Listo",
            )
            return redirect("listar-recordatorios")
        else:
            warning(
                request,
                "No se pudo eliminar el recordatorio",
                timer=3000,
                button="OK",
            )