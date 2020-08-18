from django.db import models

class Configuration(models.Model):

    email = models.EmailField(
        verbose_name="Email utilisé pour l'envoi de mail",
        unique=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.duration)

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configuration"

