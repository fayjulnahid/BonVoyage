# Generated by Django 3.2.6 on 2022-03-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_stuffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
