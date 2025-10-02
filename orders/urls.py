from django.urls import path
from . import views

urlpatterns = [
    # temporary test route
    path('test/', views.test, name='test'),
]
