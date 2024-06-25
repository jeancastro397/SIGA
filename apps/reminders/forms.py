from datetime import datetime
from django.forms import (
    ModelForm,
    TextInput,
    DateField,
    DateInput,
    TimeField,
    TimeInput,
    Select,
)
from .models import Reminder

class ReminderForm(ModelForm):
    date = DateField(
        widget=DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'placeholder': 'Seleccione una fecha'
        }),
    )
    time = TimeField(
        widget=TimeInput(attrs={
            'class': 'form-control',
            'type': 'time',
            'placeholder': 'Seleccione una hora'
        }),
    )

    class Meta:
        model = Reminder
        fields = [
            'name',  # Este campo debe estar definido en el modelo y es el nombre del recordatorio
            'note',
            'date',
            'time',
        ]
        widgets = {
            'note': Select(attrs={
                'class': 'form-control'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del recordatorio'
            }),
        }

    def save(self, commit=True):
        reminder = super().save(commit=False)
        reminder_at_date = self.cleaned_data['date']
        reminder_at_time = self.cleaned_data['time']
        reminder.remind_at = datetime.combine(reminder_at_date, reminder_at_time)
        if commit:
            reminder.save()
        return reminder
