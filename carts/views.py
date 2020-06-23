from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from artworks.models import Artwork
from .models import Order
from .cart import Cart
from .forms import CartAddArtworkForm, CartEmailForm
from rates.models import Rate
from django.core.mail import send_mail

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

@login_required
def order_confirm(request):
    cart = Cart(request)
    order = Order.objects.create(
        user = request.user,
    )
    artworks = []
    for item in cart:
        artworks.append(item['artwork'])
        artwork = Artwork.objects.get(id=item['artwork'].id)
        artwork.state = 2
        artwork.save()
    order.artworks.set(artworks)
    order.save()
    cart.clear()
    return render(
        request, 
        'carts/order_confirm.html', 
        {
            'order': order
        }
    )


def order_confirm_noaccount(request):
    if request.method == "POST":
        form = CartEmailForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            artworks = ''
            for item in cart:
                artworks += item['artwork'].name
            send_mail(
                'Demande de location',
                artworks,
                form.cleaned_data['email'],
                ['admin@email.com'],
                fail_silently=False,
            )
            cart.clear()
            return render(
                request, 
                'carts/order_confirm_noaccount.html', 
                {}
            )
    else:
        form = CartEmailForm()
    return render(
        request, 
        'carts/cart_email.html', 
        {
            'form': form
        }
    )