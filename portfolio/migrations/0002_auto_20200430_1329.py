# Generated by Django 3.0 on 2020-04-30 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='hero_position',
            new_name='hero',
        ),
    ]
