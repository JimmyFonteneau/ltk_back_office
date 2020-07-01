from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from carts.cart import Cart
from artworks.models import Artwork
from .models import Order
from .forms import OrderEmailForm
from users.models import UserProfile

def is_superuser(user=None):    
    if user == None:
        return false   
    return user.is_superuser

@login_required
def order_confirm(request):
    cart = Cart(request)
    order = Order.objects.create(
        user = request.user,
        price = cart.get_total_price()
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
        'orders/order_confirm.html', 
        {
            'order': order
        }
    )

def order_confirm_noaccount(request):
    if request.method == "POST":
        form = OrderEmailForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            url = '<a href="'+settings.ALLOWED_HOSTS[0]+'/orders/create-user-orders-'+form.cleaned_data['email']+'-'+"1"+'/">Créer l\'utilisateur et ses commandes</a>'
            send_mail(
                'Demande de location',
                url,
                form.cleaned_data['email'],
                ['admin@email.com'],
                fail_silently=False,
            )
            cart.clear()
            return render(
                request, 
                'orders/order_confirm_noaccount.html', 
                {}
            )
    else:
        form = OrderEmailForm()
    return render(
        request, 
        'orders/order_email.html', 
        {
            'form': form
        }
    )

@user_passes_test(is_superuser)
def create_user_orders(request, **kwargs):
    user = UserProfile.objects.create(
        email = kwargs['user_email'],
        username = kwargs['user_email']
    )
    artwork = Artwork.objects.get(id=kwargs['artwork_id'])
    #artwork.state = 2
    #artwork.save()
    return render( request, 'orders/create_user_orders.html', {})