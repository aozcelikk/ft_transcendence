# Generated by Django 5.0 on 2023-12-25 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_remove_kisiler_user_kisiler_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kisiler',
            old_name='users',
            new_name='user',
        ),
    ]
