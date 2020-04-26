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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"