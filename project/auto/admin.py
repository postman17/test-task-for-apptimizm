from django.contrib import admin

from .models import CarNameModel, CarModel


admin.site.register(CarNameModel)
admin.site.register(CarModel)
