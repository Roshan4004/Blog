# Generated by Django 4.0.3 on 2023-03-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='links',
            field=models.TextField(default={'facebook': 'None', 'instagram': 'None', 'twitter': 'None', 'youtube': 'None'}, null=True),
        ),
    ]
