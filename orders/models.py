from django.db import models

from users.models import UserProfile
from artworks.models import Artwork
from rates.models import Rate
import django.utils.timezone

from artworks.models import Artwork
from rates.models import Rate
from django.db import models
import django.utils.timezone

class OrderArtworkRate(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        db_index=True,
        null=False,
        blank=False,
    )
    rate = models.ForeignKey(
        Rate,
        on_delete=models.CASCADE,
        db_index=True,
        null=False,
        blank=False,
    )
    
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE,)

    return_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

class Order(models.Model):

    ORDER_STATES = (
        (1, 'En attente'),
        (2, 'Confirmée'),
        (3, 'Refusée'),
    )

    state = models.PositiveSmallIntegerField(
        choices=ORDER_STATES,
        default=2,
        blank=False,
        null=False
    )

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        db_index=True,
        null=False,
        blank=False,
        related_name='order_user'
    )

    price = models.DecimalField(
        verbose_name="Prix (€)",
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) + ' - ' + str(self.price) + '€'

    class Meta:
        abstract = False
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

