# Generated by Django 4.1 on 2022-09-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mydebtors", "0002_settings_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
