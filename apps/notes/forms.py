from django.forms import (
    ModelForm,
    TextInput,
    DateInput
)
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            "title",
            "description",
            "due_date",
        ]
        widgets = {
            "title": TextInput(attrs={
                "class":"form-control",
                "placeholder":"Ingrese el título."
            }),
            "description": TextInput(attrs={
                "class":"form-control",
                "placeholder":"Escriba su contenido aquí..."
            }),
            "due_date": DateInput(attrs={
                "class":"form-control"
            }),
        }