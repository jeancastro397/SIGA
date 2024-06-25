from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReminderForm
from .models import Reminder



def crear_recordatorio(request):
    if request.method == 'GET':
        context = {
            "title": "Crear Recordatorio",
            "reminderForm": ReminderForm()
        }
        return render(request, "reminders/crear-recordatorio.html", context)

    if request.method == 'POST':
        reminderForm = ReminderForm(data=request.POST)
        if reminderForm.is_valid():
            reminderForm.save()
            return redirect("home")

        context = {
            "title": "Crear recordatorio",
            "reminderForm": reminderForm
        }
        return render(request, "reminders/crear-recordatorio.html", context)



@login_required
def listarRecordatorio(request):
    if request.method == 'GET':
        context = {
            "title": "Lista de notas",
            "listReminders": Reminder.objects.all()
        }
        return render(request, "reminders/listar-recordatorios.html", context)