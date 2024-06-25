from datetime import datetime
from .models import Reminder
from django.forms import (
    ModelForm,
    DateField,
    DateInput,
    TimeField,
    TimeInput,
    Select,
)


class ReminderForm(ModelForm):
    date = DateField(
        widget=DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
    )
    time = TimeField(
        widget=TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        }),
    )

    class Meta:
        model = Reminder
        fields = [
            'name',
            'note',
            'date',
            'time',
        ]
        widgets = {
            'note': Select(attrs={
                'class': 'form-control'
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