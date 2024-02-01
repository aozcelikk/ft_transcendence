# Generated by Django 4.2.7 on 2023-12-03 22:39

# import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            # field=ckeditor.fields.RichTextField(),
            field=models.TextField(),
        ),
    ]
