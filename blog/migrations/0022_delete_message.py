# Generated by Django 5.0 on 2023-12-09 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
