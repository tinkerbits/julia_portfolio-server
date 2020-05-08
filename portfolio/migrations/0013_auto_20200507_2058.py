# Generated by Django 3.0 on 2020-05-07 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.base


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200506_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSuccessView',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Message')),
            ],
            bases=(django.views.generic.base.TemplateView, 'portfolio.message'),
        ),
        migrations.DeleteModel(
            name='SlackAlert',
        ),
    ]