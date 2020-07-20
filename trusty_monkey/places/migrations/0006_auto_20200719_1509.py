# Generated by Django 3.0.6 on 2020-07-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_dessertpics_insidepics_mainpics_menupics_outsidepics'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessertpics',
            name='name_1',
            field=models.CharField(default='no name', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dessertpics',
            name='name_2',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='mainpics',
            name='name_1',
            field=models.CharField(default='no name', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainpics',
            name='name_2',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='starterpics',
            name='name_1',
            field=models.CharField(default='no name', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='starterpics',
            name='name_2',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
