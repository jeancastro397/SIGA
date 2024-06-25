from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from sweetify import success, warning


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
            success(
                request,
                "Nota creada",
                text="La nota ha sido creada con éxito",
                timer=4000,
                button="Listo",
            )
            return redirect("listar-notas")
        
        warning(
            request,
            "Error al crear la nota",
            text="Revice los campo e inténtelo nuevamente.",
            timer=3000,
            button="OK",
        )
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



@login_required
def modificarNota(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)

    if request.method == 'GET':
        form = NoteForm(instance=note)
        context = {
            "title": "Modificar Nota",
            "form": form
        }
        return render(request, "notes/modificar-notas.html", context)
    
    if request.method == 'POST':
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            success(
                request,
                "Nota actualizada",
                timer=3000,
                button="Listo",
            )
            return redirect("listar-notas")
        
    warning(
        request,
        "No se pudo actualizar",
        text="Revice los campos e inténtelo nuevamente.",
        timer=5000,
        button="OK",
    )
    context = {
        "title": "Modificar Nota",
        "form": form
    }
    return render(request, "notes/modificar-notas.html", context)