from django.db import models

class Artist(models.Model):

    firstname = models.CharField(
        verbose_name="Prénom",
        max_length=200,
        blank=False,
        null=False,
    )

    lastname = models.CharField(
        verbose_name="Nom de famille",
        max_length=200,
        blank=False,
        null=False,
    )

    name = models.CharField(
        verbose_name="Nom d'artiste",
        max_length=200,
        blank=True,
        null=True,
    )

    spotlight = models.BooleanField(
        verbose_name="Mise en avant",
        default=False,
    )

    artist_description = models.CharField(
        verbose_name="Description de l'artiste",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    artist_universe = models.CharField(
        verbose_name="Description de l'artiste",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Artiste"
        verbose_name_plural = "Artistes"