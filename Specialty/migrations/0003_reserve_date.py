# Generated by Django 4.2 on 2023-12-26 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Specialty', '0002_remove_reserve_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 12, 26)),
        ),
    ]
