from django.urls import path
from .views import ProductListView, ProductDetailView
from .views import UserRegistrationView
from core.views import UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # New route
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/token/', obtain_auth_token, name='api-token'),
]
