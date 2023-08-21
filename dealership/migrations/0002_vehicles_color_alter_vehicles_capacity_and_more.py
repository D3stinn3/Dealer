# Generated by Django 4.2.4 on 2023-08-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='capacity',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='car_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]