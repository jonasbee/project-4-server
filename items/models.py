from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    icon = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.name}'

class InventoryItem(models.Model):
    expiry_date = models.DateField()
    # is_shared = models.BooleanField()
    quantity_number = models.PositiveIntegerField()
    metric = models.CharField(max_length=15)
    item = models.ForeignKey(
        Item,
        related_name='item',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'jwt_auth.User',
        related_name='created_inventory_items',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user}\'s {self.item}'