# Generated by Django 5.0 on 2023-12-20 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_kisiler_kategoriler_alter_kisiler_resim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiler',
            name='arkadaslar',
            field=models.ManyToManyField(blank=True, to='blog.kisiler'),
        ),
        migrations.CreateModel(
            name='ArkadasIstek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arkadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arkadas', to='blog.kisiler')),
                ('sahip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sahip', to='blog.kisiler')),
            ],
        ),
    ]