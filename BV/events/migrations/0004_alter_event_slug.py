# Generated by Django 3.2.6 on 2022-03-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='event-slug', max_length=120, unique=True),
        ),
    ]
