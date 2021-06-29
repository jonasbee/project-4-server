#from django.shortcuts import render
#import items
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Item, InventoryItem
from .serializers import (
    ItemSerializer, 
    InventoryItemSerializer, 
    PopulatedInventoryItemSerializer
)

# Create your views here.
class ItemsListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        items = Item.objects.all()
        serialized_items = ItemSerializer(items, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)

class InventoryItemsListView(APIView):

    permission_classes = (IsAuthenticated, )

    # TODO: should only work for logged in users
    def get(self, request, user_pk):
        try:
            inventory_items = InventoryItem.objects.filter(user_id=user_pk)
            # get(user_id=user_pk)
            if inventory_items[0].user != request.user:
                raise PermissionDenied()
            serialized_inventory_items = PopulatedInventoryItemSerializer(inventory_items, many=True)
            return Response(serialized_inventory_items.data, status=status.HTTP_200_OK)
        except InventoryItem.DoesNotExist:
            raise NotFound()
        # or get all inventory_items, for item in []
        # if item.user['id'] ...
    
class InventoryItemCreateView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        # _user_pk
        # TODO: where to get the user.id and item.id from
        # user.id in token logged in with
        #print(request.data['user'])
        #print(request.user)
        #print(request.user.id)
        request.data['user'] = request.user.id
        #request.data['item'] = request.item.id
        new_inventory_item = InventoryItemSerializer(data=request.data)
        if new_inventory_item.is_valid():
            new_inventory_item.save()
            return Response(new_inventory_item.data, status=status.HTTP_201_CREATED)
        return Response(new_inventory_item.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class InventoryItemDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def put(self, request, inv_item_pk):
        try:
            inventory_item_to_update = InventoryItem.objects.get(pk=inv_item_pk)
            if inventory_item_to_update.user != request.user:
                raise PermissionDenied()
            request.data['user'] = request.user.id
            updated_inventory_item = InventoryItemSerializer(inventory_item_to_update, data=request.data)
            if updated_inventory_item.is_valid():
                updated_inventory_item.save()
                return Response(updated_inventory_item.data, status=status.HTTP_202_ACCEPTED)
            return Response(updated_inventory_item.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except InventoryItem.DoesNotExist:
            raise NotFound()

    def delete(self, request, inv_item_pk):
        inventory_item_to_delete = InventoryItem.objects.get(pk=inv_item_pk)
        #print(user_pk)
        if inventory_item_to_delete.user != request.user:
        # request.user
            raise PermissionDenied()
        inventory_item_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        