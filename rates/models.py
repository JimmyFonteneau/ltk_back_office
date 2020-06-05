from django.db import models

class Rate(models.Model):

    duration = models.DecimalField(
        verbose_name="Durée en mois",
        max_digits=2, 
        decimal_places=0,
        blank=False,
        null=False,
    )
    
    rate = models.DecimalField(
        verbose_name="Taux",
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False,
    )
    
    def __str__(self):
        return "Taux"+str(self.rate)

    class Meta:
        verbose_name = "Taux"
        verbose_name_plural = "Taux"
