# Generated by Django 3.0.8 on 2020-07-20 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_auto_20200720_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessertpics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
        migrations.AlterField(
            model_name='dessertpics',
            name='restaurant_review_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='insidepics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
        migrations.AlterField(
            model_name='insidepics',
            name='restaurant_review_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='mainpics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
        migrations.AlterField(
            model_name='mainpics',
            name='restaurant_review_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
        migrations.AlterField(
            model_name='menupics',
            name='restaurant_review_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='outsidepics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
        migrations.AlterField(
            model_name='outsidepics',
            name='restaurant_review_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantReview'),
        ),
        migrations.AlterField(
            model_name='starterpics',
            name='maps_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='places.RestaurantId'),
        ),
    ]
