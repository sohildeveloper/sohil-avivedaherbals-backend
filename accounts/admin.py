from django.contrib import admin
from .models import User

@admin.register(User)      # decorator way of registering
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
