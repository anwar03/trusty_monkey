# Generated by Django 3.0.6 on 2020-07-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='adress',
            field=models.CharField(default='empty adress', max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='maps_id',
            field=models.CharField(max_length=140),
        ),
    ]
