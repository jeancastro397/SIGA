from django.shortcuts import render, redirect
from .forms import NoteForm


def nota(request):
    contexto = {
        "form" : NoteForm()
    }

    if request.method == 'POsT':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
        
        else:
            contexto['form'] = form
    
    return render(request, 'nota.html', contexto)


