# Generated by Django 3.2.8 on 2021-11-10 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import valetapp.models.booking


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChainStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('rating', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=15)),
                ('discount', models.DecimalField(decimal_places=15, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Valet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffId', models.UUIDField(blank=True, default=uuid.uuid4, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='valetapp.membershiptype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('booking_state', models.CharField(choices=[('PENDING', 'pending'), ('BOOKED', 'booked'), ('CANCELLED', 'cancelled'), ('END_TIME', 'endtime')], default=valetapp.models.booking.BookingStates['PENDING'], max_length=20)),
                ('carReg', models.DecimalField(decimal_places=15, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valetapp.customer')),
                ('valetservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valetapp.valet')),
            ],
        ),
    ]
