# Generated by Django 4.2 on 2023-12-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Specialty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='Date',
        ),
    ]
