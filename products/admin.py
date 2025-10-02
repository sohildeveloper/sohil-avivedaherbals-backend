from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'description')