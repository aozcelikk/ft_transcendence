# Generated by Django 5.0 on 2023-12-20 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_kisiler_arkadaslar_arkadasistek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kisiler',
            name='arkadaslar',
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, to='blog.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='blog.customuser')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='blog.customuser')),
            ],
        ),
        migrations.DeleteModel(
            name='ArkadasIstek',
        ),
    ]
