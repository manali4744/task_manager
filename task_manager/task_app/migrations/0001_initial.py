# Generated by Django 3.2.18 on 2023-04-11 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='email address')),
                ('name', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(message='invalid name', regex='^[A-Za-z]{2,25}$')])),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
