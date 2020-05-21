from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from artworks.models import Artwork
from .cart import Cart
from .forms import CartAddArtworkForm

@require_POST
def cart_add(request, artwork_id):
    cart = Cart(request)
    artwork = get_object_or_404(Artwork, id=artwork_id)
    form = CartAddArtworkForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            artwork=artwork,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('carts:cart_detail')

def cart_remove(request, artwork_id):
    cart = Cart(request)
    artwork = get_object_or_404(Artwork, id=artwork_id)
    cart.remove(artwork)
    return redirect('carts:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddArtworkForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True
                }
            )
    return render(
        request, 
        'carts/cart_detail.html', 
        {
            'cart': cart
        }
    )