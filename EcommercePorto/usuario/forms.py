from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile

class AuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password",
                'placeholder' : "Contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]

class UserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "username",
                'placeholder' : "Nombre Usuario"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "first_name",
                'placeholder' : "Nombre"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "last_name",
                'placeholder' : "Apellido"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "email",
                'id' : "email",
                'placeholder' : "Correo Electronico"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password1",
                'placeholder' : "Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "password",
                'id' : "password2",
                'placeholder' : "Confirme su contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]