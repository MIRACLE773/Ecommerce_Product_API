from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer

class OrderListView(generics.ListAPIView):
    """
    List all orders of the authenticated user
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single order
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrderView(generics.CreateAPIView):
    """
    Create a new order from the authenticated user's cart
    """
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
