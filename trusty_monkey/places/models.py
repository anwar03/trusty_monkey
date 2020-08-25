from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime    
        
        
class Restaurant(models.Model):
    maps = models.CharField(primary_key=True, max_length=140, unique=True)
    adress = models.CharField(max_length=240)
    lat = models.FloatField(default='0000000')
    lng = models.FloatField(default='0000000')
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class RestaurantReview(models.Model):    
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE)    
    maps = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):        
        return str(self.id)


class StarterPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                               on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40, null=True, blank=True)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
   
    class Meta: 
        verbose_name = 'StarterPics'
        verbose_name_plural = 'StarterPics'


class MainPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                               on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40, null=True, blank=True)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
   
    class Meta: 
        verbose_name = 'MainPics'
        verbose_name_plural = 'MainPics'

class DessertPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40, null=True, blank=True)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)    

    class Meta: 
        verbose_name = 'DessertPics'
        verbose_name_plural = 'DessertPics'


class MenuPic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
   
    class Meta: 
        verbose_name = 'MenuPics'
        verbose_name_plural = 'MenuPics'


class OutsidePic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name = 'OutsidePics'
        verbose_name_plural = 'OutsidePics'


class InsidePic(models.Model):
    restaurant_review = models.ForeignKey(RestaurantReview,
                                                on_delete=models.CASCADE)
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name = 'InsidePics'
        verbose_name_plural = 'InsidePics'