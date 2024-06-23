from django.shortcuts import render, redirect
from .forms import ReminderForm

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
