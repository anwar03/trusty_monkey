# Generated by Django 3.0.8 on 2020-07-20 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20200719_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessertpics',
            name='maps_id',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insidepics',
            name='maps_id',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainpics',
            name='maps_id',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menupics',
            name='maps_id',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outsidepics',
            name='maps_id',
            field=models.CharField(default='none', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='starterpics',
            name='maps_id',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]
