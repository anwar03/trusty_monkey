from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from places.api.permissions import (IsAuthorOrReadOnly,
                                    IsOwnReviewOrReadOnly)
from places import models
from . import serializers
from drf_multiple_model.views import (FlatMultipleModelAPIView,
                                    ObjectMultipleModelAPIView)


class RestaurantIdViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantIdSerializer


class RestaurantReviewViewset(viewsets.ModelViewSet):
    queryset = models.RestaurantReview.objects.all()
    # serializer_class = serializers.RestaurantReviewSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.RestaurantReviewGETSerializer # your above serializer
        else:
            return serializers.RestaurantReviewSerializer # default serializer

    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(review_author=self.request.user)

# class NewRestaurantReviewViewset(viewsets.ModelViewSet):
#     queryset = models.RestaurantReview.objects.all()
#     serializer_class = serializers.NewRestaurantReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(review_author=self.request.user)


class StarterPicsViewset(viewsets.ModelViewSet):
    queryset = models.StarterPic.objects.all()
    serializer_class = serializers.StarterPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


class MainPicsViewset(viewsets.ModelViewSet):
    queryset = models.MainPic.objects.all()
    serializer_class = serializers.MainPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

       
class DessertPicsViewset(viewsets.ModelViewSet):
    queryset = models.DessertPic.objects.all()
    serializer_class = serializers.DessertPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class MenuPicsViewset(viewsets.ModelViewSet):
    queryset = models.MenuPic.objects.all()
    serializer_class = serializers.MenuPicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class OutsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.OutsidePic.objects.all()
    serializer_class = serializers.OutsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]

    
class InsidePicsViewset(viewsets.ModelViewSet):
    queryset = models.InsidePic.objects.all()
    serializer_class = serializers.InsidePicsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnReviewOrReadOnly]


class UserReviewListAPIView(generics.ListAPIView):
    serializer_class = serializers.RestaurantReviewSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.RestaurantReview.objects.filter(
                                review_author=kwarg_user)


class RestaurantReviewListAPIView(generics.ListAPIView):
    serializer_class = serializers.RestaurantReviewSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.RestaurantReview.objects.filter(
                                restaurant=kwarg_restaurant)


class UserSarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.StarterPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MainPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.DessertPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.MenuPic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.OutsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class UserInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_user = self.kwargs.get('user')
        return models.InsidePic.objects.filter(
                                restaurant_review__review_author=kwarg_user)


class RestaurantStarterPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.StarterPicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.StarterPic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class RestaurantMainPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MainPicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.MainPic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class RestaurantDessertPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.DessertPicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.DessertPic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class RestaurantMenuPicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.MenuPicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.MenuPic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class RestaurantOutsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.OutsidePicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.OutsidePic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class RestaurantInsidePicsListAPIView(generics.ListAPIView):
    serializer_class = serializers.InsidePicsSerializer

    def get_queryset(self):
        kwarg_restaurant = self.kwargs.get('restaurant')       
        return models.InsidePic.objects.filter(
                                restaurant_review__restaurant=kwarg_restaurant)


class AllEveryRestPicturesAPIView(FlatMultipleModelAPIView):
    querylist = [
        {'queryset': models.StarterPic.objects.all(),
                        'serializer_class': serializers.StarterPicsSerializer},
        {'queryset': models.MainPic.objects.all(),
                        'serializer_class': serializers.MainPicsSerializer},
        {'queryset': models.DessertPic.objects.all(),
                        'serializer_class': serializers.DessertPicsSerializer},
        {'queryset': models.MenuPic.objects.all(),
                        'serializer_class': serializers.MenuPicsSerializer},
        {'queryset': models.OutsidePic.objects.all(),
                        'serializer_class': serializers.OutsidePicsSerializer},
        {'queryset': models.InsidePic.objects.all(),
                        'serializer_class': serializers.InsidePicsSerializer},
    ]


class AllUserPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_user = self.kwargs.get('user')

        querylist = (
            {'queryset': 
            models.StarterPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset': 
            models.DessertPic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset': 
            models.MenuPic.objects.filter(restaurant_review__review_author=kwarg_user),    
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset': 
            models.OutsidePic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset': 
            models.InsidePic.objects.filter(restaurant_review__review_author=kwarg_user),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


class AllSingleRestPicturesAPIView(FlatMultipleModelAPIView):

    def get_querylist(self):
        kwarg_restaurant = self.kwargs.get('restaurant')

        querylist = (
            {'queryset':
            models.StarterPic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset':
            models.DessertPic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset':
            models.MenuPic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset':
            models.OutsidePic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset':
            models.InsidePic.objects.filter(restaurant_review__restaurant=kwarg_restaurant),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist


class AllReviewPicturesAPIView(ObjectMultipleModelAPIView):

    def get_querylist(self):
        kwarg_review = self.kwargs.get('review')

        querylist = (
            {'queryset':
            models.StarterPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.StarterPicsSerializer},
            {'queryset':
            models.MainPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.MainPicsSerializer},
            {'queryset':
            models.DessertPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.DessertPicsSerializer},
            {'queryset':
            models.MenuPic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.MenuPicsSerializer},
            {'queryset':
            models.OutsidePic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.OutsidePicsSerializer},
            {'queryset':
            models.InsidePic.objects.filter(restaurant_review=kwarg_review),
                        'serializer_class': serializers.InsidePicsSerializer},
        )

        return querylist
