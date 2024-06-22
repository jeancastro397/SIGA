from django.contrib.auth.models import User
from apps.notes.models import Note
from django.db.models import (
    Model,
    ForeignKey,
    DateTimeField,
    CASCADE
)
from django.utils import timezone


class Reminder(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    note = ForeignKey(Note, on_delete=CASCADE)
    remind_at = DateTimeField(default=timezone.now)
    created_ad = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.note.title}"
