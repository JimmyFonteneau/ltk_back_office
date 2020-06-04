from django.db import models

from artworks.models import Artwork
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Order(models.Model):

    artworks = models.ManyToManyField(
        Artwork,
        verbose_name = "Oeuvres",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name = "Utilisateur",
        db_index=True,
        null=False,
        blank=False,
    )

    created_at = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"