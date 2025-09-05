from django.urls import path
from .views import CartRetrieveView, AddCartItemView, UpdateCartItemView, RemoveCartItemView

urlpatterns = [
    path('', CartRetrieveView.as_view(), name='cart-detail'),
    path('add/', AddCartItemView.as_view(), name='cart-add'),
    path('item/<int:item_id>/update/', UpdateCartItemView.as_view(), name='cart-item-update'),
    path('item/<int:item_id>/remove/', RemoveCartItemView.as_view(), name='cart-item-remove'),
]