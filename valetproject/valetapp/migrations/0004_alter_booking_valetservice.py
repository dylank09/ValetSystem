# Generated by Django 3.2.8 on 2021-11-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valetapp', '0003_alter_booking_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='valetservice',
            field=models.CharField(default='', max_length=200),
        ),
    ]
