from django.db import models

from users.models import UserProfile
from artworks.models import Artwork

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

    artworks = models.ManyToManyField(Artwork, related_name='order_artwork')

    def __str__(self):
        return str(self.user) + ' - ' + str(self.price) + '€'

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"