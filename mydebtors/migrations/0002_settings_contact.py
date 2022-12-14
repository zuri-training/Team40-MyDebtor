# Generated by Django 4.1 on 2022-09-20 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mydebtors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
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
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("website", models.URLField()),
                ("facebook", models.URLField()),
                ("twitter", models.URLField()),
                ("phone1", models.CharField(max_length=13)),
                ("phone2", models.CharField(max_length=13)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
