# Generated by Django 3.0.6 on 2020-07-19 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20200719_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarterPics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_1', models.ImageField(upload_to='')),
                ('lat_pic_1', models.FloatField()),
                ('lng_pic_1', models.FloatField()),
                ('shot_time_1', models.DateTimeField()),
                ('picture_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('lat_pic_2', models.FloatField(blank=True, null=True)),
                ('lng_pic_2', models.FloatField(blank=True, null=True)),
                ('shot_time_2', models.DateTimeField(blank=True, null=True)),
                ('restaurant_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview')),
            ],
        ),
    ]
