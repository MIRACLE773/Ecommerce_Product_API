from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404


class CartRetrieveView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddCartItemView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()

        return Response(
            CartSerializer(cart, context={'request': request}).data,
            status=status.HTTP_201_CREATED
        )


class UpdateCartItemView(generics.UpdateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'item_id'

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)


class RemoveCartItemView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'item_id'

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)
