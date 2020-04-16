from django.db import models

from artworks.models import Artwork
from users.models import UserProfile

class Cart(models.Model):

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name = "Utilisateur",
        db_index=True,
        null=False,
        blank=False,
    )

    artworks = models.ManyToManyField(Artwork)
