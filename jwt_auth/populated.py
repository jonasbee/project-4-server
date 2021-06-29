from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from items.serializers import InventoryItemSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    created_inventory_items = InventoryItemSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'profile_image',
            'email',
            'preference',
            'created_inventory_items',
        )