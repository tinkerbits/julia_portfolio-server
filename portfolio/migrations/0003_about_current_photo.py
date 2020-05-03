# Generated by Django 3.0 on 2020-05-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_about_current_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='current_photo',
            field=models.CharField(choices=[('disabled', 'disabled'), ('enabled', 'enabled')], default='disabled', error_messages={'unique': 'Another artwork already uses this hero position.'}, max_length=8),
        ),
    ]