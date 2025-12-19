"""URL configuration for the shop application.

Maps URL patterns to their corresponding views. Uses class-based views
imported from ``shop.views`` and associates a namespace for reverse lookups.
"""

from django.urls import path

from .views import (
    HomeView,
    CategoryDetailView,
    ProductDetailView,
    ProductListView,
)

app_name = "shop"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("category/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
]
