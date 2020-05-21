from decimal import Decimal
from django.conf import settings
from artworks.models import Artwork

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, artwork, quantity=1, update_quantity=False):
        artwork_id = str(artwork.id)
        if artwork_id not in self.cart:
            self.cart[artwork_id] = {'quantity': 0,
                                    'price': str(artwork.price)}
        if update_quantity:
            self.cart[artwork_id]['quantity'] = quantity
        else:
            self.cart[artwork_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, artwork):
        artwork_id = str(artwork.id)
        if artwork_id in self.cart:
            del self.cart[artwork_id]
            self.save()

    def __iter__(self):
        artwork_ids = self.cart.keys()
        artworks = Artwork.objects.filter(id__in=artwork_ids)
        for artwork in artworks:
            self.cart[str(artwork.id)]['artwork'] = artwork

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True