# Generated by Django 2.2.10 on 2020-08-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_background',
            field=models.ImageField(blank=True, default='/default.jpg', null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='content',
            name='concept_firstblock_img',
            field=models.ImageField(blank=True, default='/default.jpg', null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_content_img',
            field=models.ImageField(blank=True, default='/default.jpg', null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='content',
            name='homepage_first_img',
            field=models.ImageField(blank=True, default='/default.jpg', null=True, upload_to='static'),
        ),
    ]
