from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


# Crear las notas estando logeado
@login_required
def crearNota(request):
    if request.method == 'GET':
        context = {
            "title": "Nueva nota",
            "form": NoteForm
        }
        return render(request, "notes/crear-nota.html", context)
    
    if request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("listar-notas")
        
        context = {
            "title": "Nueva nota",
            "form": form
        }
        return render(request, "notes/crear-nota.html", context)



# Listar las notas 
@login_required
def listarNota(request):
    if request.method == 'GET':
        context = {
            "title": "Lista de notas",
            "listNotes": Note.objects.all()
        }
        return render(request, "notes/listar-notas.html", context)