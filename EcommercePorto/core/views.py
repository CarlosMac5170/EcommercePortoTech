from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from cart.forms import CartAddProductForm

# Create your views here.
def home(request):
    cantidad = 0
    cart = Cart(request)
    for item in cart:
        cantidad = cantidad + 1
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'core/home.html', {'cantidad': cantidad})

def about(request):
    cantidad = 0
    cart = Cart(request)
    for item in cart:
        cantidad = cantidad + 1
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'core/about.html', {'cantidad': cantidad})