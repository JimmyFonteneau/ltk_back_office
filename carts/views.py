from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from artworks.models import Artwork
from .models import Order
from .cart import Cart
from .forms import CartAddArtworkForm
from rates.models import Rate

@require_POST
def cart_add(request, artwork_id):
    cart = Cart(request)
    artwork = get_object_or_404(Artwork, id=artwork_id)
    form = CartAddArtworkForm(request.POST)
    if form.is_valid():
        cart.add(
            artwork=artwork,
            nb_month=form.cleaned_data['nb_month'].duration,
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
        rate = Rate.objects.get(duration=item['nb_month'])
        item['update_nb_month_form'] = CartAddArtworkForm(
            initial= {
                'nb_month': rate,
            }
        )
    return render(
        request, 
        'carts/cart_detail.html', 
        {
            'cart': cart
        }
    )