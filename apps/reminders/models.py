from django.contrib.auth.models import User
from apps.notes.models import Note
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    DateTimeField,
    CASCADE
)
from django.utils import timezone


class Reminder(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    note = ForeignKey(Note, on_delete=CASCADE)
    name = CharField(max_length=30, null=False, blank=False)
    remind_at = DateTimeField(default=timezone.now)
    created_ad = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.note.title}"
    
    # models.py
from django.db import models

class Recordatorio(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

