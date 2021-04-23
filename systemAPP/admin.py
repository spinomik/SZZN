from django.contrib import admin
from .models import Driver, MenuCategories, Menu, Warehouse

admin.site.register(Driver)
admin.site.register(MenuCategories)
admin.site.register(Menu)

@admin.register(Warehouse)
class WarehouseView(admin.ModelAdmin):
    fields = ('meal_name', 'quantity', 'delivery_date')
