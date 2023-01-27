from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
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
                'placeholder' : "Correo electronico"
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "address",
                'placeholder' : "Dirección"
            }
        )
    )

    postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "postal_code",
                'placeholder' : "Codigo Postal"
            }
        )
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : "text",
                'id' : "city",
                'placeholder' : "Ciudad"
            }
        )
    )
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
