# shop/urls.py
from django.urls import path

app_name = "shop"

from .views import home_view, category_detail_view, product_detail_view, product_list_view

urlpatterns = [
    path("", home_view, name="home"),
    path("products/", product_list_view, name="product_list"),
    path("category/<slug:slug>/", category_detail_view, name="category_detail"),
    path("product/<slug:slug>/", product_detail_view, name="product_detail"),
]