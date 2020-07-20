from django.urls import include, path
from rest_framework import routers
from places.api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'restaurant_id', myapp_views.RestaurantIdViewset)
router.register(r'restaurant_reviews', myapp_views.RestaurantReviewViewset)
router.register(r'starter_pics', myapp_views.StarterPicsViewset)
router.register(r'main_pics', myapp_views.MainPicsViewset)
router.register(r'dessert_pics', myapp_views.DessertPicsViewset)
router.register(r'menu_pics', myapp_views.MenuPicsViewset)
router.register(r'outside_pics', myapp_views.OutsidePicsViewset)
router.register(r'inside_pics', myapp_views.InsidePicsViewset)

urlpatterns = [
    path('', include(router.urls))
]