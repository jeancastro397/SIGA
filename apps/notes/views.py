from django.shortcuts import render, redirect
from .forms import NoteForm


def crearNota(request):
    contexto = {
        "form" : NoteForm()
    }

    if request.method == 'POsT':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
        
        else:
            contexto['form'] = form
    
    return render(request, 'notes/crear-nota.html', contexto)


