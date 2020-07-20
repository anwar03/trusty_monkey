from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime    


class RestaurantId(models.Model):
    maps_id = models.CharField(max_length=140, unique=True)
    adress = models.CharField(max_length=240)
    lat = models.FloatField(default='0000000')
    lng = models.FloatField(default='0000000')
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name
        

class RestaurantReview(models.Model):    
    review_author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE)    
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - Author: {}, Place visited: {}'.format(self.id, self.review_author, self.restaurant_id)


class StarterPics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                               on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
    name_2 = models.CharField(max_length=40, null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    lat_pic_2 = models.FloatField(null=True, blank=True)
    lng_pic_2 = models.FloatField(null=True, blank=True)
    shot_time_2 = models.DateTimeField(null=True, blank=True)

    class Meta: 
        verbose_name = 'StarterPics'
        verbose_name_plural = 'StarterPics'


class MainPics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                               on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
    name_2 = models.CharField(max_length=40, null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    lat_pic_2 = models.FloatField(null=True, blank=True)
    lng_pic_2 = models.FloatField(null=True, blank=True)
    shot_time_2 = models.DateTimeField(null=True, blank=True)

    class Meta: 
        verbose_name = 'MainPics'
        verbose_name_plural = 'MainPics'

class DessertPics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                                on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=40)    
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
    name_2 = models.CharField(max_length=40, null=True, blank=True)
    picture_2 = models.ImageField(null=True, blank=True)
    lat_pic_2 = models.FloatField(null=True, blank=True)
    lng_pic_2 = models.FloatField(null=True, blank=True)
    shot_time_2 = models.DateTimeField(null=True, blank=True)

    class Meta: 
        verbose_name = 'DessertPics'
        verbose_name_plural = 'DessertPics'


class MenuPics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                                on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)  
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)
    picture_2 = models.ImageField()
    lat_pic_2 = models.FloatField(default='0000000')
    lng_pic_2 = models.FloatField(default='0000000')
    shot_time_2 = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name = 'MenuPics'
        verbose_name_plural = 'MenuPics'


class OutsidePics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                                on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE) 
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name = 'OutsidePics'
        verbose_name_plural = 'OutsidePics'


class InsidePics(models.Model):
    restaurant_review_id = models.OneToOneField(RestaurantReview,
                                                on_delete=models.CASCADE)
    pics_author = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(RestaurantId, on_delete=models.CASCADE)   
    picture_1 = models.ImageField()
    lat_pic_1 = models.FloatField(default='0000000')
    lng_pic_1 = models.FloatField(default='0000000')
    shot_time_1 = models.DateTimeField(default=datetime.now)

    class Meta: 
        verbose_name = 'InsidePics'
        verbose_name_plural = 'InsidePics'