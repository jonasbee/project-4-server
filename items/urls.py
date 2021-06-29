from django.urls import path
from .views import (
    ItemsListView,
    InventoryItemsListView,
    InventoryItemCreateView,
    InventoryItemDetailView,
)

urlpatterns = [
    path('', ItemsListView.as_view()),
    path('<int:user_pk>/inventory/', InventoryItemsListView.as_view()),
    path('inventory/new/', InventoryItemCreateView.as_view()),
    path('inventory/<int:inv_item_pk>/', InventoryItemDetailView.as_view()),
]