# Generated by Django 3.2.6 on 2022-04-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='slug',
            field=models.SlugField(default='slug', max_length=120),
        ),
    ]
