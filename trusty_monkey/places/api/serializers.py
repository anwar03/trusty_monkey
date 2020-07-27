from places.models import (Restaurant, RestaurantReview,
                           StarterPic, MainPic,
                           DessertPic, MenuPic,
                           OutsidePic, InsidePic)
from rest_framework import serializers
from django.db.models import Q


class RestaurantIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        field = fields = '__all__'


class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        field = fields = '__all__'

    def validate_restaurant_review_id(self, value):        
        if value.review_author != self.context['request'].user:                       
            raise serializers.ValidationError("User has not reviewed the restaurant")        
        return value



class StarterPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarterPic
        fields = '__all__'

    def validate_restaurant_review_id(self, value):        
        if value.review_author != self.context['request'].user:                       
            raise serializers.ValidationError("User has not reviewed the restaurant")        
        return value
   

class MainPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPic
        fields = '__all__'

    def validate_restaurant_review_id(self, value):
        print(value.id)         
        if value.review_author != self.context['request'].user or not RestaurantReview.objects.filter(id=value.id, 
                                               restaurant_id=value.restaurant_id).exists():            
            raise serializers.ValidationError("User has not reviewed the restaurant")
        print('WTF2')
        
        # if RestaurantReview.objects.filter(id=value.id, 
        #                                        restaurant_id=value.restaurant_id).exists():              
        #     print('filters working')
        return value
        # print('WTF3')       
        # raise serializers.ValidationError('Not the right restaurant')


class DessertPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertPic
        fields = '__all__'

    def validate_restaurant_review_id(self, value):        
        if value.review_author != self.context['request'].user:            
            raise serializers.ValidationError("User has not reviewed the restaurant")        
        return value


class MenuPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPic
        fields = '__all__'

    def validate_restaurant_review_id(self, value):        
        if value.review_author != self.context['request'].user:            
            raise serializers.ValidationError("User has not reviewed the restaurant")        
        return value


class OutsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsidePic
        fields = '__all__'

    def validate_restaurant_review_id(self, value):        
        if value.review_author != self.context['request'].user:            
            raise serializers.ValidationError("User has not reviewed the restaurant")        
        return value


class InsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsidePic
        field = fields = '__all__'

    # def validate_restaurant_review_id(self, value):        
    #     if value.review_author != self.context['request'].user:            
    #         raise serializers.ValidationError("User has not reviewed the restaurant")        
    #     return value

    def validate_restaurant_review(self, value):
        user = self.context['request'].user
    
        if not value in user.restaurantreview_set.values_list('restaurant_id', flat=True): # since RestaurantReview has restaurant field 
            raise serializers.ValidationError('User has not reviewed the restaurant')        
        return value