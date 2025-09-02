from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all(), write_only=True, required=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'category_id', 'price', 'stock_quantity', 'image']
