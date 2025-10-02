from django.urls import path
from . import views
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    # temporary test route
    path('test/', views.test, name='test'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
