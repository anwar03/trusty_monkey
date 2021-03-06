# Generated by Django 3.0.8 on 2020-07-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20200720_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessertpics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='dessertpics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='insidepics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='insidepics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='mainpics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='mainpics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='lat_pic_2',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='lng_pic_2',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='outsidepics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='outsidepics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='restaurantid',
            name='lat',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='restaurantid',
            name='lng',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='starterpics',
            name='lat_pic_1',
            field=models.FloatField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='starterpics',
            name='lng_pic_1',
            field=models.FloatField(default='0000000'),
        ),
    ]
