# Generated by Django 3.2.8 on 2021-11-17 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import valetapp.models.item
import valetapp.models.subject


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
                ('maxNumberOfValetsPerHour', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=15)),
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
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('valetservice', models.CharField(default='', max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valetapp.chainstore')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valetapp.customer')),
            ],
            bases=(models.Model, valetapp.models.subject.Subject, valetapp.models.item.Item),
        ),
    ]
