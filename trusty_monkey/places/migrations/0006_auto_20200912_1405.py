# Generated by Django 3.0.8 on 2020-09-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_restaurant_opening_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='opening_hours',
            field=models.CharField(max_length=440),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]