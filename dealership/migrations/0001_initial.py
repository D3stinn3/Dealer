# Generated by Django 4.2.4 on 2023-08-16 12:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)])),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(6)])),
                ('wallet', models.IntegerField(default=0)),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='dealership.area')),
                ('car_dealer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20, null=True, unique=True)),
                ('car_price', models.FloatField(max_length=10, null=True)),
                ('capacity', models.CharField(max_length=2)),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dealership.area')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dealership.cardealer')),
            ],
        ),
    ]
