# Generated by Django 5.0 on 2023-12-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_friendrequest_to_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='ekle',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], default='accepted', max_length=8),
        ),
    ]