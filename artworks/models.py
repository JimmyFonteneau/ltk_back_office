from django.db import models

from artists.models import Artist

class Artwork(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    height = models.DecimalField(
        verbose_name="Hauteur (cm)",
        max_digits=4, 
        decimal_places=1,
        blank=False,
        null=False,
    )

    width = models.DecimalField(
        verbose_name="Largeur (cm)",
        max_digits=4, 
        decimal_places=1,
        blank=False,
        null=False,
    )

    price = models.DecimalField(
        verbose_name="Prix (€)",
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False,
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name = "Artiste",
        db_index=True,
        null=False,
        blank=False,
    )

    photo = models.ImageField(upload_to='artworks', default='/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oeuvre"
        verbose_name_plural = "Oeuvres"