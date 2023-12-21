from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    SellerListCreateAPIView,
    SellerDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    CustomerListCreateAPIView,
    CustomerDetailAPIView,
    CartListCreateAPIView,
    CartDetailAPIView,
    WishlistListCreateAPIView,
    WishlistDetailAPIView,
    TodoDetailAPIView,
    TodoListCreateAPIView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    # Seller URLs
    path('sellers/', SellerListCreateAPIView.as_view(), name='seller-list'),
    path('sellers/<int:pk>/', SellerDetailAPIView.as_view(), name='seller-detail'),

    # Product URLs
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # Customer URLs
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),

    # Cart URLs
    path('carts/', CartListCreateAPIView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartDetailAPIView.as_view(), name='cart-detail'),

    # Wishlist URLs
    path('wishlists/', WishlistListCreateAPIView.as_view(), name='wishlist-list'),
    path('wishlists/<int:pk>/', WishlistDetailAPIView.as_view(), name='wishlist-detail'),
    
     # Todo URLs
    path('Todo/', TodoListCreateAPIView.as_view(), name='Todo-list'),
    path('Todo/<int:pk>/', TodoDetailAPIView.as_view(), name='Todo-detail'),
]
