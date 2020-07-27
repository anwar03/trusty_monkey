# Generated by Django 3.0.8 on 2020-07-27 14:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0018_auto_20200720_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='DessertPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'DessertPics',
                'verbose_name_plural': 'DessertPics',
            },
        ),
        migrations.CreateModel(
            name='InsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'InsidePics',
                'verbose_name_plural': 'InsidePics',
            },
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'MainPics',
                'verbose_name_plural': 'MainPics',
            },
        ),
        migrations.CreateModel(
            name='MenuPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('picture_2', models.ImageField(upload_to='')),
                ('lat_pic_2', models.FloatField(default='0000000')),
                ('lng_pic_2', models.FloatField(default='0000000')),
                ('shot_time_2', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'MenuPics',
                'verbose_name_plural': 'MenuPics',
            },
        ),
        migrations.CreateModel(
            name='OutsidePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'OutsidePics',
                'verbose_name_plural': 'OutsidePics',
            },
        ),
        migrations.CreateModel(
            name='StarterPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=40)),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField(default='0000000')),
                ('lng_pic_1', models.FloatField(default='0000000')),
                ('shot_time_1', models.DateTimeField(default=datetime.datetime.now)),
                ('name_2', models.CharField(blank=True, max_length=40, null=True)),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'StarterPics',
                'verbose_name_plural': 'StarterPics',
            },
        ),
        migrations.RenameModel(
            old_name='RestaurantId',
            new_name='Restaurant',
        ),
        migrations.RemoveField(
            model_name='insidepics',
            name='pics_author',
        ),
        migrations.RemoveField(
            model_name='insidepics',
            name='restaurant_id',
        ),
        migrations.RemoveField(
            model_name='insidepics',
            name='restaurant_review_id',
        ),
        migrations.RemoveField(
            model_name='mainpics',
            name='pics_author',
        ),
        migrations.RemoveField(
            model_name='mainpics',
            name='restaurant_id',
        ),
        migrations.RemoveField(
            model_name='mainpics',
            name='restaurant_review_id',
        ),
        migrations.RemoveField(
            model_name='menupics',
            name='pics_author',
        ),
        migrations.RemoveField(
            model_name='menupics',
            name='restaurant_id',
        ),
        migrations.RemoveField(
            model_name='menupics',
            name='restaurant_review_id',
        ),
        migrations.RemoveField(
            model_name='outsidepics',
            name='pics_author',
        ),
        migrations.RemoveField(
            model_name='outsidepics',
            name='restaurant_id',
        ),
        migrations.RemoveField(
            model_name='outsidepics',
            name='restaurant_review_id',
        ),
        migrations.RemoveField(
            model_name='starterpics',
            name='pics_author',
        ),
        migrations.RemoveField(
            model_name='starterpics',
            name='restaurant_id',
        ),
        migrations.RemoveField(
            model_name='starterpics',
            name='restaurant_review_id',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='maps_id',
            new_name='maps',
        ),
        migrations.RenameField(
            model_name='restaurantreview',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.DeleteModel(
            name='DessertPics',
        ),
        migrations.DeleteModel(
            name='InsidePics',
        ),
        migrations.DeleteModel(
            name='MainPics',
        ),
        migrations.DeleteModel(
            name='MenuPics',
        ),
        migrations.DeleteModel(
            name='OutsidePics',
        ),
        migrations.DeleteModel(
            name='StarterPics',
        ),
        migrations.AddField(
            model_name='starterpic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='outsidepic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='menupic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='mainpic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='insidepic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AddField(
            model_name='dessertpic',
            name='restaurant_review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
    ]