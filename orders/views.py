from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from carts.cart import Cart
from artworks.models import Artwork
from .models import Order, OrderArtworkRate
from .forms import OrderEmailForm, OrderUpdate, ReturnDateUpdate
from users.models import UserProfile
import random, string
from rates.models import Rate
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from configuration.models import Configuration

def is_superuser(user=None):    
    if user == None:
        return false   
    return user.is_superuser


def create_order(request, user):
    cart = Cart(request)
    order = Order.objects.create(
        user = user,
        price = cart.get_total_price(),
        state = 1
    )
    order.save()
    for item in cart:
        artwork = Artwork.objects.get(id=item['artwork'].id)
        rate = Rate.objects.get(duration=item['nb_month'])
        order_artwork_rate = OrderArtworkRate.objects.create(
            artwork = artwork,
            rate = rate,
            order = order,
            return_date = datetime.now() + relativedelta(months=+rate.duration)
        )
        order_artwork_rate.save()
    cart.clear()

    configuration = Configuration.objects.all().first() 
    accept = settings.ALLOWED_HOSTS[1]+'orders/accept-order-'+str(order.id)
    refuse = settings.ALLOWED_HOSTS[1]+'orders/deny-order-'+str(order.id)
    
    subject = 'Demande de location'
    data = {'accept': accept, 'refuse': refuse, 'email': user.email, 'cart': cart, 'total': cart.get_total_price() }
    html_message = render_to_string('./mails/request_mail.html', data)
    plain_message = strip_tags(html_message)
    from_email = 'plateforme@ltk.com'
    to = configuration.email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    return order


@login_required
def order_confirm(request):
    order = create_order(request, request.user)
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
            user = UserProfile.objects.create(
                email = form.cleaned_data['email'],
                username = form.cleaned_data['email'],
                password = ''.join(random.choices(string.ascii_uppercase + string.digits))
            )
            user.save()
            order = create_order(request, user)
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


def accept_order(request, **kwargs):
    order = Order.objects.get(id=kwargs['order_id'])
    order.state = 2
    order.save()
    order_artwork_rates = OrderArtworkRate.objects.filter(order=order)
    for order_artwork_rate in order_artwork_rates:
        artwork = Artwork.objects.get(id=order_artwork_rate.artwork.id)
        artwork.state = 2
        artwork.save()
    return render(request, 'orders/accept_order.html', {})

def deny_order(request, **kwargs):
    order = Order.objects.get(id=kwargs['order_id'])
    order.state = 3
    order.save()
    return render(request, 'orders/deny_order.html', {})


def order_update(request, order_id):             
    order = Order.objects.get(id=order_id)
    rates = Rate.objects.all()
    order_artwork_rates = OrderArtworkRate.objects.filter(order=order)
    order.artworks = []
    for order_artwork_rate in order_artwork_rates:
        order.artworks.append(order_artwork_rate)
    if request.method == 'POST':
        if 'delete_order' in request.POST:
            order.delete()          
            return redirect("orders:orders_list")
        else:
            form = OrderUpdate(request.POST, instance=order)
            if form.is_valid(): 
                data = {'accept': False, 'id': order.id }
                if(form.cleaned_data['state'] == 2):
                    data = {'accept': True , 'id': order.id }
                    order_artwork_rates = OrderArtworkRate.objects.filter(order=order)
                    for order_artwork_rate in order_artwork_rates:
                        artwork = Artwork.objects.get(id=order_artwork_rate.artwork.id)
                        artwork.state = 2
                        artwork.save()                
                
                subject = 'Demande de location'                
                html_message = render_to_string('./mails/order_response.html', data)
                plain_message = strip_tags(html_message)
                from_email = 'plateforme@ltk.com'
                to = order.user.email
                send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                
                form.save()
                return redirect("orders:orders_list")
    else:
        form = OrderUpdate(instance=order)  
    return render(
        request,
        'orders/order_update.html',
        {
            'form': form,
            'order': order,
            'rates': rates,
        }
    ) 


def orders_list(request):
    orders = Order.objects.all()
    if request.user.is_superuser:
        return render(
            request,
            'orders/orders_list.html',
            {
                'orders_list': orders,
            }
        )

def change_return_date(request, order_id):
    order_artwork_rates = OrderArtworkRate.objects.get(id=order_id)
    print('order_artwork_rates.artwork_id')
    print(order_artwork_rates.artwork_id)
    artwork = Artwork.objects.get(id=order_artwork_rates.artwork_id)
    
    if request.method == 'POST':                
        form = ReturnDateUpdate(request.POST, instance=order_artwork_rates)
        if form.is_valid(): 
            form.save()
            return redirect("orders:orders_list")
    else:
        form = ReturnDateUpdate(instance=order_artwork_rates) 
    return render(
        request,
        'orders/update_return_date.html',
        {
            'order_artwork_rates': order_artwork_rates,
            'form': form,
            'artworkd': artwork,
        }
    )