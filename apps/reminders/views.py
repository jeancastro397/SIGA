from django.shortcuts import render, redirect
from .forms import ReminderForm


def crear_recordatorio(request):
    context = {
        'recordatorio': ReminderForm()
    }

    if request.method == 'POST':
        recordatorio = ReminderForm(data=request.POST)
        if recordatorio.is_valid:
            recordatorio.save()
        else:
            context['recordatorio'] = recordatorio
    
    return render (request, 'reminders/crear-recordatorio.html', context)
