# Generated by Django 3.2.6 on 2022-04-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='type',
            field=models.CharField(choices=[('ac', 'AC'), ('nonac', 'Non AC'), ('Sleeper', 'Sleeper')], default='nonac', max_length=120),
        ),
    ]
