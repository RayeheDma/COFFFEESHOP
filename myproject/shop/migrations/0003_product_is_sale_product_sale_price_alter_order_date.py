# Generated by Django 5.0.6 on 2024-06-25 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 25, 19, 6, 19, 935258)),
        ),
    ]
