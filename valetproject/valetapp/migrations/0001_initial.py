# Generated by Django 3.2.8 on 2021-10-27 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='customer', max_length=28)),
                ('surname', models.CharField(default='surname', max_length=28)),
                ('password', models.CharField(default='abc123', max_length=50)),
                ('email', models.CharField(default='customer@gmail.com', max_length=50)),
                ('colour', models.CharField(max_length=23)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ValetService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valetType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='customer', max_length=28)),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('surname', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('colour', models.CharField(max_length=23, null=True)),
                ('membershipType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='valetapp.membershiptype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carReg', models.DecimalField(decimal_places=15, max_digits=20)),
                ('valetservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valetapp.valetservice')),
            ],
        ),
    ]
