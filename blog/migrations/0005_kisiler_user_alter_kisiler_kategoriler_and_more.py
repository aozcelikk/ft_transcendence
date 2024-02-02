# Generated by Django 5.0 on 2023-12-14 12:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_kisiler_kategori_kisiler_kategoriler'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiler',
            name='user',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kisiler',
            name='kategoriler',
            field=models.ManyToManyField(blank=True, to='blog.kategori'),
        ),
        migrations.AlterField(
            model_name='kisiler',
            name='kullanici',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='kisiler',
            name='tam_adi',
            field=models.CharField(max_length=150),
        ),
    ]