# Generated by Django 5.0.6 on 2024-06-19 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 19, 20, 19, 48, 55312)),
        ),
    ]