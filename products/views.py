from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

def test(request):
    return JsonResponse({"message": "Products API working!"})

# List all products / Create product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

# Retrieve / Update / Delete product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
