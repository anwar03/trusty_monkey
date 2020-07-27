from django.urls import include, path
from rest_framework import routers
from places.api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'restaurant', myapp_views.RestaurantIdViewset)
router.register(r'restaurant_review', myapp_views.RestaurantReviewViewset)
router.register(r'starter_pic', myapp_views.StarterPicsViewset)
router.register(r'main_pic', myapp_views.MainPicsViewset)
router.register(r'dessert_pic', myapp_views.DessertPicsViewset)
router.register(r'menu_pic', myapp_views.MenuPicsViewset)
router.register(r'outside_pic', myapp_views.OutsidePicsViewset)
router.register(r'inside_pic', myapp_views.InsidePicsViewset)

urlpatterns = [
    path('', include(router.urls))
]