from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductSingleView.as_view(), name='product_single'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.BlogSingleView.as_view(), name='blog_single'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]