# Generated by Django 5.0 on 2023-12-13 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_kategori_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiler',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.kategori'),
        ),
    ]
