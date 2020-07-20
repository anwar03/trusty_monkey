from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from places.api.permissions import IsOwnReviewOrReadOnly, IsAuthorOrReadOnly
from places import models
from . import serializers

class RestaurantIdViewset(viewsets.ModelViewSet):
    queryset = models.RestaurantId.objects.all()
    serializer_class = serializers.RestaurantIdSerializer

class RestaurantReviewViewset(viewsets.ModelViewSet):
    queryset = models.RestaurantReview.objects.all()
    serializer_class = serializers.RestaurantReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(review_author=self.request.user)

class StarterPicsViewset(viewsets.ModelViewSet):
    queryset = models.StarterPics.objects.all()
    serializer_class = serializers.StarterPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)

class MainPicsViewset(viewsets.ModelViewSet):
    queryset = models.MainPics.objects.all()
    serializer_class = serializers.MainPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)

class DessertPicsViewset(viewsets.ModelViewSet):
    queryset = models.DessertPics.objects.all()
    serializer_class = serializers.DessertPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)

class MenuPicsViewset(viewsets.ModelViewSet):
    queryset = models.MenuPics.objects.all()
    serializer_class = serializers.MenuPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)

class OutsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.OutsidePics.objects.all()
    serializer_class = serializers.OutsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)

class InsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.InsidePics.objects.all()
    serializer_class = serializers.InsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnReviewOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(pics_author=self.request.user)