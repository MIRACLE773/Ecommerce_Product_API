from rest_framework import serializers
from .models import Order, OrderItem
from cart.serializers import CartItemSerializer
from cart.models import Cart

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'product_id', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'status', 'created_at']
        read_only_fields = ['user', 'total_price', 'created_at', 'items']


class CreateOrderSerializer(serializers.Serializer):
    """
    Serializer to create an order from a user's cart.
    """
    def create(self, validated_data):
        user = self.context['request'].user
        cart = Cart.objects.get(user=user)
        order = Order.objects.create(user=user, total_price=cart.total)

        # Create OrderItems
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product_name=item.product.name,
                product_id=item.product.id,
                price=item.product.price,
                quantity=item.quantity
            )

        # Clear the cart after order creation
        cart.items.all().delete()

        return order
