from rest_framework import serializers
from .models import CartItem
from products.models import Product

# Small product serializer for embedding in CartItem
class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "image"]

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductMiniSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "user", "product", "quantity", "added_at"]
