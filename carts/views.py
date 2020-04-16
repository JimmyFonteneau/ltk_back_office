from django.shortcuts import render, redirect
from .models import Cart
from artworks.models import Artwork
from users.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect
    
def cart_add(request):
    artwork_id = request.POST['artwork_id']
    artwork = Artwork.objects.get(id=artwork_id) 
    if request.is_ajax() and request.method == 'POST':
        cartExist = Cart.objects.filter(user_id=request.user.id).exists()
        if cartExist == False:
            cart = Cart(user=request.user)
            cart.save()
            cart.artworks.add(artwork)
            count = len(cart.artworks.filter())
            print(count)
            return HttpResponse(count)
        else:
            cartByUser = Cart.objects.get(user_id=request.user.id)
            cartByUser.artworks.add(artwork)
            count = len(cartByUser.artworks.filter())
            print(count)
            return HttpResponse(count)
    else:
        raise Http404

def cart_length(request):
    cartExist = Cart.objects.filter(user_id=request.user.id).exists()
    if cartExist == False:
        raise Http404
    else:
        cartByUser = Cart.objects.get(user_id=request.user.id)
        count = len(cartByUser.artworks.filter())
        return HttpResponse(count)
    
def cart_delete(request):
    artwork_id = request.POST['artwork_id']
    artwork = Artwork.objects.get(id=artwork_id)
    cartExist = Cart.objects.filter(user_id=request.user.id).exists()
    if cartExist == False:
        raise Http404
    else:
        cartByUser = Cart.objects.get(user_id=request.user.id)
        cartByUser.artworks.remove(artwork)
        return HttpResponse(True)
    return HttpResponse(True)

def cart(request):
    cartExist = Cart.objects.filter(user_id=request.user.id).exists()
    if cartExist == False:
        raise Http404
    else:
        cartByUser = Cart.objects.get(user_id=request.user.id)
        return render(
            request, 
            'carts/mycart.html', 
            {
                'cart': cartByUser,
                'artworks': cartByUser.artworks.all(),
            }
        )