# <<<<<<< HEAD
# Generated by Django 4.1 on 2022-08-09 14:57
# =======
# Generated by Django 4.0.5 on 2022-08-09 15:14
# >>>>>>> c56f3d07e687e23780a703f1a15e5f7927d2e9b8

import core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mydebtors.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(default=mydebtors.models.reg_number_generator, max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('student_class', models.CharField(max_length=255)),
                ('passport', models.ImageField(default='default.jpg', upload_to=mydebtors.models.get_passport_path)),
                ('nationality', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=550)),
                ('date_of_birth', models.DateField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('state', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=550)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='mydebtors.student')),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=10)),
                ('term', models.CharField(choices=[('first', '1st Term'), ('second', '2nd Term'), ('third', '3rd Term')], max_length=20)),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('outstanding_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('tutition', 'tutition'), ('damage', 'damage')], max_length=255)),
                ('status', models.CharField(choices=[('active', 'active'), ('pending', 'pending'), ('resolved', 'resolved')], default='active', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debt', to='mydebtors.student')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('proof', models.FileField(blank=True, null=True, upload_to=mydebtors.models.get_complaint_path, validators=[core.validators.validate_file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'pdf', 'png'])])),
                ('status', models.CharField(choices=[('cleared', 'cleared'), ('pending', 'pending')], default='pending', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('debt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='mydebtors.debt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
