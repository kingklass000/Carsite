from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(CarPhotos)
admin.site.register(Rating)
admin.site.register(Review)
