from django.db import models

class Content(models.Model):
    
    homepage_title = models.CharField(
        verbose_name="Titre page d'accueil",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    homepage_first_img = models.ImageField(upload_to='static', null=True, blank=True, verbose_name="Première image page d'accueil",)

    homepage_title_description = models.CharField(
        verbose_name="Titre bloc page d'accueil",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    homepage_content_description = models.TextField(
        verbose_name="Contenu bloc page d'accueil",
        blank=False,
        null=False,
        default='default',
    )

    homepage_content_img = models.ImageField(upload_to='static', null=True, blank=True, verbose_name="Image central page d'accueil",)


    concept_firstblock_title = models.CharField(
        verbose_name="Titre premier bloc concept",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    concept_firstblock_content = models.TextField(
        verbose_name="Titre du second bloc concept",
        blank=False,
        null=False,
        default='default',
    )

    concept_firstblock_background = models.ImageField(upload_to='static', null=True, blank=True, verbose_name="Première image background concept",)

    concept_firstblock_img = models.ImageField(upload_to='static', null=True, blank=True, verbose_name="Image premier bloc concept")
    
    concept_secondblock_title = models.CharField(
        verbose_name="Titre du second bloc concept",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    concept_secondblock_content = models.TextField(
        verbose_name="Contenu du second bloc concept",
        blank=False,
        null=False,
        default='default',
    )

    concept_thirdblock_title = models.CharField(
        verbose_name="Titre du troisième bloc concept",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    concept_thirdblock_firstservice = models.CharField(
        verbose_name="Contenu premier service",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )
    
    concept_thirdblock_secondservice = models.CharField(
        verbose_name="Contenu second service",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    concept_thirdblock_thirdservice = models.CharField(
        verbose_name="Contenu troisième service",
        max_length=200,
        blank=False,
        null=False,
        default='default',
    )

    def __str__(self):
        return "Content"

    class Meta:
        verbose_name = "Contenu du site"
        verbose_name_plural = "Contenus du site"
