from decimal import Decimal
from django.conf import settings
from artworks.models import Artwork
from rates.models import Rate

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, artwork, nb_month):
        nb_month = str(nb_month)
        artwork_id = str(artwork.id)
        if artwork_id not in self.cart:
            self.cart[artwork_id] = {
                'nb_month': nb_month,
                'price': str(artwork.price)
            }
        self.cart[artwork_id]['nb_month'] = int(nb_month)
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
            rate = Rate.objects.get(duration=item['nb_month'])
            item['price'] = Decimal(item['price'])
            item['total_price'] = round(item['price'] * item['nb_month'] / 3 * rate.rate, 2)
            yield item

    def __len__(self):
        return len(self.cart.values())

    def get_total_price(self):
        return round(sum(Decimal(item['price']) * item['nb_month'] / 3 * Rate.objects.get(duration=item['nb_month']).rate for item in self.cart.values()), 2)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True