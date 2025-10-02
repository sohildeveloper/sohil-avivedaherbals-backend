from django.urls import path
from .views import test, CartItemListCreateView, CartItemDetailView

urlpatterns = [
    # temporary test route
    path('test/', test, name='test'),
    path("", CartItemListCreateView.as_view(), name="cart-list-create"),
    path("<int:pk>/", CartItemDetailView.as_view(), name="cart-detail"),
]
