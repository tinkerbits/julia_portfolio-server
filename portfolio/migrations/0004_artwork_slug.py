# Generated by Django 3.0 on 2020-05-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_artwork_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
