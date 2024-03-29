# Generated by Django 5.0 on 2023-12-26 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arkadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diger_users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sahip', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Engel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kisi', models.CharField(default=False, max_length=250)),
                ('diger_users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kisiengel', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kisiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici', models.CharField(max_length=150)),
                ('tam_adi', models.CharField(max_length=150)),
                ('resim', models.ImageField(blank=True, default='blogs/7.jpg', upload_to='blogs')),
                ('toplam_mac', models.IntegerField(default=0)),
                ('zafer_mac', models.IntegerField(default=0)),
                ('bozgun_mac', models.IntegerField(default=0)),
                ('cevrimici', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
