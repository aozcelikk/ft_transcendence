# Generated by Django 5.0 on 2023-12-23 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_kisiler_arkadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisiler',
            name='arkadas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.arkadas'),
        ),
    ]
