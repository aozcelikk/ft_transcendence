# Generated by Django 5.0 on 2023-12-14 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_kisiler_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisiler',
            name='resim',
            field=models.ImageField(default='images/blogs/7.jpg', upload_to='blogs'),
        ),
    ]