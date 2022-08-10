# Generated by Django 4.1 on 2022-08-10 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydebtors', '0002_alter_debt_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='school',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='debt',
            name='outstanding_fee',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='debt',
            name='total_fee',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
