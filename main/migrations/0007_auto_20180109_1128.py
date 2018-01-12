# Generated by Django 2.0 on 2018-01-09 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180109_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='staff',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_arrival_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 28, 32, 137139)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_departure_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 28, 32, 137158)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 28, 32, 137104)),
        ),
    ]
