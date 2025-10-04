from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_id", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "user", "total_price", "status", "created_at", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        total = 0
        for item in items_data:
            product_id = item["product_id"]
            qty = item["quantity"]
            price = item["price"]

            OrderItem.objects.create(order=order, product_id=product_id, quantity=qty, price=price)
            total += qty * float(price)

        order.total_price = total
        order.save()
        return order
