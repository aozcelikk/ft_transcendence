# Generated by Django 5.0 on 2023-12-23 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_remove_kisiler_engel_arkadas_engel'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiler',
            name='arkadas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.arkadas'),
        ),
    ]