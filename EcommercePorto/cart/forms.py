from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), coerce=int, label='Cantidad')
        
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
