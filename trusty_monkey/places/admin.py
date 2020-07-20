from django.contrib import admin
from places.models import (RestaurantReview, StarterPics,
                           MainPics, DessertPics, MenuPics,
                           OutsidePics, InsidePics,
                           RestaurantId)
# Register your models here.

admin.site.register(RestaurantId)
admin.site.register(RestaurantReview)
admin.site.register(StarterPics)
admin.site.register(MainPics)
admin.site.register(DessertPics)
admin.site.register(MenuPics)
admin.site.register(OutsidePics)
admin.site.register(InsidePics)