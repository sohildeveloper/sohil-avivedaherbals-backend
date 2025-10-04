from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

def test(request):
    return JsonResponse({"message": "Orders API working!"})

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all().prefetch_related("items")
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Order.objects.filter(user_id=user_id).prefetch_related("items")
        return Order.objects.none()


class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all().prefetch_related("items")
    serializer_class = OrderSerializer
