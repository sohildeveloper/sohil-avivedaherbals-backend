from rest_framework import generics, status
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from django.http import JsonResponse

def test(request):
    return JsonResponse({"message": "Carts API working!"})

class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return CartItem.objects.filter(user_id=user_id).select_related("product")
        return CartItem.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.data.get("user")
        product = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))

        # check if product already in cart for this user
        cart_item, created = CartItem.objects.get_or_create(
            user_id=user, product_id=product,
            defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all().select_related("product")
    serializer_class = CartItemSerializer
