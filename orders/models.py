from django.db import models

from users.models import UserProfile
from artworks.models import Artwork

class Order(models.Model):

    UserProfile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name = "Artiste",
        db_index=True,
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        verbose_name="Prix (€)",
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False,
    )

    artworks = models.ManyToManyField(Artwork)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oeuvre"
        verbose_name_plural = "Oeuvres"