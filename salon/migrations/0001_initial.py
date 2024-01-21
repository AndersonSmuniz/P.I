# Generated by Django 5.0.1 on 2024-01-21 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Salon",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("image", models.URLField(blank=True)),
                ("password", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("type", models.CharField(max_length=20)),
                ("coordinates", models.CharField(max_length=255)),
                (
                    "salon_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="salon_location",
                        to="salon.salon",
                    ),
                ),
            ],
        ),
    ]
