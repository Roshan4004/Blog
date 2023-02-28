# Generated by Django 4.0.3 on 2023-02-10 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cmnt_likes',
            field=models.ManyToManyField(blank=True, related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
