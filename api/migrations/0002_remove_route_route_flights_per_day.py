# Generated by Django 2.0.4 on 2019-02-07 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='route_flights_per_day',
        ),
    ]