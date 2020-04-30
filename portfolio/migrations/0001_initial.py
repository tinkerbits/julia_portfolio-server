# Generated by Django 3.0 on 2020-04-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ImageField(upload_to='artworks/%Y')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('hero', models.IntegerField(blank=True, choices=[(1, 'left'), (2, 'center'), (3, 'right')], error_messages={'unique': 'Another artwork already uses this hero position.'}, null=True, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
