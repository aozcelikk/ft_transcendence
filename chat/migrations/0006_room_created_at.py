# Generated by Django 5.0 on 2024-02-19 17:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_delete_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]