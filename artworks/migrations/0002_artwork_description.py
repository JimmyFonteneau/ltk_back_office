# Generated by Django 2.2.10 on 2020-08-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='description',
            field=models.CharField(default='default', max_length=200, verbose_name="Description de l'oeuvre"),
        ),
    ]
