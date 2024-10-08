# Generated by Django 4.2.13 on 2024-07-31 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Catalog",
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
                ("name", models.CharField(max_length=255)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("camera", models.TextField(blank=True, null=True)),
                ("lens", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("index", models.IntegerField(blank=True, null=True)),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="portfolio/photos/")),
                ("description", models.TextField(blank=True, null=True)),
                ("exposure", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "focal_distance",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("iso", models.IntegerField(blank=True, null=True)),
                ("is_cover_image", models.BooleanField(default=False)),
                (
                    "catalog",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portfolio.catalog",
                    ),
                ),
            ],
        ),
    ]
