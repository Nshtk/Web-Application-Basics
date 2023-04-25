from django.contrib import admin
from .models import User, Product, ProductInstance, Manufacturer, FurnitureType, Headquarter

admin.site.register(User)
admin.site.register(Headquarter)
admin.site.register(Manufacturer)
admin.site.register(FurnitureType)
admin.site.register(Product)
admin.site.register(ProductInstance)
