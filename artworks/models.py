from django.db import models

from artists.models import Artist
from rates.models import Rate

class Artwork(models.Model):

    ARTWORK_STATES = (
        (1, 'Non loué'),
        (2, 'Loué'),
    )

    state = models.PositiveSmallIntegerField(
        choices=ARTWORK_STATES,
        default=1,
        blank=True,
        null=True, )

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
        decimal_places=0,
        blank=False,
        null=False,
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name = "Artiste",
        db_index=True,
        null=True,
        blank=True,
    )

    style = models.ForeignKey(
        "Artwork_Style",        
        on_delete=models.CASCADE,
        verbose_name = "Style",
        db_index=True,
        null=True,
        blank=True,
        default='',
    )

    category = models.ForeignKey(
        "Artwork_Category",        
        on_delete=models.CASCADE,
        verbose_name = "Catégorie",
        db_index=True,
        null=True,
        blank=True,
        default='',
    )

    storage_place = models.ForeignKey(
        "Artwork_Storage_Place",        
        on_delete=models.CASCADE,
        verbose_name = "Lieu de stockage",
        db_index=True,
        null=True,
        blank=True,
        default='',
    )

    spotlight = models.BooleanField(
        verbose_name="Mise en avant",
        default=False,
    )

    photo = models.ImageField(
        upload_to='artworks', 
        default='/default.jpg'
    )

    timer = models.DateField(
        verbose_name="Timer",
        null=True,
        blank=True,
    )

    description = models.CharField(
        verbose_name="Description de l'oeuvre",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )
    
    introduction = models.CharField(
        verbose_name="Description de l'oeuvre",
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
        verbose_name = "Oeuvre"
        verbose_name_plural = "Oeuvres"

class Artwork_Style(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Style de l'oeuvre"
        verbose_name_plural = "Style des oeuvres"

class Artwork_Category(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie de l'oeuvre"
        verbose_name_plural = "Catégories des oeuvres"

class Artwork_Storage_Place(models.Model):

    name = models.CharField(
        verbose_name="Nom",
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lieu de stockage de l'oeuvre"
        verbose_name_plural = "Lieux de stockage des oeuvres"