from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

class UserProfile(AbstractUser):

    email = models.EmailField(
        'Email', 
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"