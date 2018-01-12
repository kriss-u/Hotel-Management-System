# Generated by Django 2.0 on 2018-01-09 05:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180109_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservation_customer', to='main.Customer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_arrival_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 33, 39, 205285)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_departure_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 33, 39, 205304)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 33, 39, 205251)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='staff',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservation_staff', to='main.Staff'),
        ),
        migrations.AlterField(
            model_name='room',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_customer', to='main.Reservation'),
        ),
    ]
