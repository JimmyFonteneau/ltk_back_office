# Generated by Django 2.2.10 on 2020-08-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_artist_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(default='/default.jpg', upload_to='artists'),
        ),
    ]
