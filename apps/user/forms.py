from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    Form,
    CharField,
    PasswordInput,
    EmailInput,
    TextInput
)

# Formulario de registro
# No requiere de modelos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    EmailInput,
    PasswordInput,
    TextInput
)

# Formulario de registro
class RegistroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control'}
        self.fields['first_name'].widget.attrs = {'class': 'form-control'}
        self.fields['last_name'].widget.attrs = {'class': 'form-control'}
        self.fields['email'].widget.attrs = {'class': 'form-control'}
        self.fields['password1'].widget.attrs = {'class': 'form-control'}
        self.fields['password2'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email', 
            'password1', 
            'password2'
        ]

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }




class LoginForm(Form):
    username = CharField(
        max_length=150,
        widget=TextInput(attrs={
            'placeholder': 'Nombre de Usuario',
            'class': 'form-control',
        })
    )
    password = CharField(
        widget=PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control',
        })
    )
