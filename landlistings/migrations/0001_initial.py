# Generated by Django 5.0.1 on 2024-02-09 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LandListing",
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
                ("title", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("sqft", models.IntegerField()),
                ("lot_size", models.DecimalField(decimal_places=1, max_digits=5)),
                ("description", models.TextField(blank=True)),
                (
                    "list_date",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
                ("photo_main", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                ("is_published", models.BooleanField(default=True)),
            ],
        ),
    ]