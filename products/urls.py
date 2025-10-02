from django.urls import path
from . import views
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    # temporary test route
    path('test/', views.test, name='test'),
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]


# GET http://127.0.0.1:8000/api/products/ → list products
# POST http://127.0.0.1:8000/api/products/ → create new product
# GET http://127.0.0.1:8000/api/products/1/ → get single product
# PUT/PATCH http://127.0.0.1:8000/api/products/1/ → update product
# DELETE http://127.0.0.1:8000/api/products/1/ → delete product