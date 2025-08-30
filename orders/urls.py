from django.urls import path
from .views import OrderCreateView, OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),  # GET all orders
    path('create/', OrderCreateView.as_view(), name='order_create'),  # POST new order
    path('<int:id>/', OrderDetailView.as_view(), name='order_detail'),  # GET or PATCH single order
]
