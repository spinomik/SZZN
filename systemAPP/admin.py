from django.contrib import admin
from .models import Driver, MealCategories, Meal, Warehouse, Delivery

admin.site.register(Driver)
admin.site.register(MealCategories)
admin.site.register(Meal)
admin.site.register(Delivery)

@admin.register(Warehouse)
class WarehouseView(admin.ModelAdmin):
    fields = ('delivery_ID', 'meal_name', 'quantity')
