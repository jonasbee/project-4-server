from django.contrib import admin
from .models import Item, InventoryItem

# Register your models here.
admin.site.register(Item)
admin.site.register(InventoryItem)