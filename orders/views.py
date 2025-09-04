from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer


class OrderListView(generics.ListAPIView):
    """
    List all orders of the authenticated user
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single order
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrderView(generics.CreateAPIView):
    """
    Create a new order from the authenticated user's cart
    """
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save creates the order (returns the instance)
        order = serializer.save()

        # Use OrderSerializer to return full order details
        output_serializer = OrderSerializer(order, context={"request": request})
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

