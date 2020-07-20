# Generated by Django 3.0.8 on 2020-07-20 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20200720_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessertpics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='insidepics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='mainpics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='shot_time_2',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='outsidepics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='starterpics',
            name='shot_time_1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
