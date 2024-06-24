from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import (
    ModelForm,
    Form,
    CharField,
    PasswordInput,
    EmailInput,
    TextInput,
)
from django.core.exceptions import ValidationError


# Formulario de registro
class RegistroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs = {"class": "form-control"}
        self.fields["first_name"].widget.attrs = {"class": "form-control"}
        self.fields["last_name"].widget.attrs = {"class": "form-control"}
        self.fields["email"].widget.attrs = {"class": "form-control"}
        self.fields["password1"].widget.attrs = {"class": "form-control"}
        self.fields["password2"].widget.attrs = {"class": "form-control"}

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya está en uso.")
        return email


class LoginForm(Form):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                "placeholder": "Nombre de Usuario",
                "class": "form-control",
            }
        ),
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control",
            }
        )
    )


class PerfilForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "email": EmailInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este email ya está en uso.")
        return email


class PasswordUpdateForm(PasswordChangeForm):
    old_password = CharField(
        widget=PasswordInput(attrs={"class": "form-control"}),
    )
    new_password1 = CharField(
        widget=PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = CharField(
        widget=PasswordInput(attrs={"class": "form-control"}),
    )
