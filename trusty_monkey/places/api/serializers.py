from places.models import (RestaurantId, RestaurantReview,
                           StarterPics, MainPics,
                           DessertPics, MenuPics,
                           OutsidePics, InsidePics)
from rest_framework import serializers


class RestaurantIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantId
        field = fields = '__all__'


class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        field = fields = '__all__'


class StarterPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarterPics
        fields = '__all__'


class MainPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPics
        fields = '__all__'


class DessertPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertPics
        fields = '__all__'


class MenuPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPics
        fields = '__all__'


class OutsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsidePics
        fields = '__all__'


class InsidePicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsidePics
        field = fields = '__all__'                
