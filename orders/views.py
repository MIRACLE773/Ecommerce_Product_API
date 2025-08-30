from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from products.models import Product


# Place order
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        products_data = request.data.get('products', [])
        if not products_data:
            return Response({'error': 'No products provided'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)
        total = 0
        for item in products_data:
            product = Product.objects.get(id=item['product_id'])
            quantity = item.get('quantity', 1)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
            total += product.price * quantity

        order.total_price = total
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List user orders
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# Retrieve/update/cancel single order
class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

