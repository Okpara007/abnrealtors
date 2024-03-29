# Generated by Django 5.0.1 on 2024-02-14 22:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("landlistings", "0002_remove_landlisting_sqft_landlisting_sqm_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landlisting",
            name="photo_main",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, verbose_name="image"
            ),
        ),
    ]
