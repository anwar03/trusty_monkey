from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from places.api.permissions import IsAuthorOrReadOnly
from places import models
from . import serializers

class RestaurantIdViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantIdSerializer


class RestaurantReviewViewset(viewsets.ModelViewSet):
    queryset = models.RestaurantReview.objects.all()
    serializer_class = serializers.RestaurantReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(review_author=self.request.user)


class StarterPicsViewset(viewsets.ModelViewSet):
    queryset = models.StarterPic.objects.all()
    serializer_class = serializers.StarterPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MainPicsViewset(viewsets.ModelViewSet):
    queryset = models.MainPic.objects.all()
    serializer_class = serializers.MainPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

       
class DessertPicsViewset(viewsets.ModelViewSet):
    queryset = models.DessertPic.objects.all()
    serializer_class = serializers.DessertPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class MenuPicsViewset(viewsets.ModelViewSet):
    queryset = models.MenuPic.objects.all()
    serializer_class = serializers.MenuPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class OutsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.OutsidePic.objects.all()
    serializer_class = serializers.OutsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class InsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.InsidePic.objects.all()
    serializer_class = serializers.InsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

   