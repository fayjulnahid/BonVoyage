# Generated by Django 3.2.6 on 2022-03-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20220318_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
            preserve_default=False,
        ),
    ]
