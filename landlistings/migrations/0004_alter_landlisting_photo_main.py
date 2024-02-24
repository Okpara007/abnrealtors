# Generated by Django 5.0.1 on 2024-02-24 20:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("landlistings", "0003_alter_landlisting_photo_main"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landlisting",
            name="photo_main",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, verbose_name="main_image"
            ),
        ),
    ]
