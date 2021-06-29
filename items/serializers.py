#from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Item, InventoryItem

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'preference', 'profile_image')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class PopulatedInventoryItemSerializer(InventoryItemSerializer):
    item = ItemSerializer()
    user = UserSerializer()