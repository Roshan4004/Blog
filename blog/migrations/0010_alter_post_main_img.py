# Generated by Django 4.0.3 on 2023-02-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='main_img',
            field=models.ImageField(unique=True, upload_to='blog/media/uploads'),
        ),
    ]
