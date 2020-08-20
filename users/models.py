from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class UserProfile(AbstractUser):

    email = models.EmailField(
        'Email', 
        unique=True
    )
    firstname = models.CharField(
        verbose_name="Prénom",
        max_length=256,
        blank=False,
        null=False,
    )
    lastname = models.CharField(
        verbose_name="Nom de famille",
        max_length=256,
        blank=False,
        null=False,
    )
    company = models.CharField(
        verbose_name="Entreprise",
        max_length=256,
        blank=True,
        null=True,
        default='default company',
    )
    phone = models.IntegerField(
        verbose_name="Téléphone",
        blank=True,
        null=True,
        default='0000000000',
    )

    updated_password = models.BooleanField(
        default=False,
        blank=False,
        null=False,        
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.firstname+" "+self.lastname

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"