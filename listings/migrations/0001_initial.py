# Generated by Django 5.0.1 on 2024-02-11 01:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=200)),
                ("house_type", models.CharField(blank=True, max_length=200)),
                ("address", models.CharField(blank=True, max_length=200)),
                ("city", models.CharField(blank=True, max_length=100)),
                ("state", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                ("price", models.IntegerField(blank=True)),
                ("bedrooms", models.IntegerField()),
                (
                    "bathrooms",
                    models.DecimalField(blank=True, decimal_places=1, max_digits=2),
                ),
                ("sqm", models.IntegerField(blank=True, default=0)),
                (
                    "lot_size",
                    models.DecimalField(blank=True, decimal_places=1, max_digits=5),
                ),
                (
                    "photo_main",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_3",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_4",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_5",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_6",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                ("is_published", models.BooleanField(default=True)),
                (
                    "list_date",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]