# Generated by Django 4.0.3 on 2023-01-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=30, unique=True),
        ),
    ]
