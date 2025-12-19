"""
Views for the shop application.

This module implements class-based views to handle the home page, category
listing, product details and the product listing. Using generic views
provides extensibility and built-in pagination support. At the bottom
of the module we expose function aliases for backwards compatibility.
"""

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import Category, Product


class HomeView(TemplateView):
    """Display the home page with featured categories and latest products."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):  # type: ignore[override]
        context = super().get_context_data(**kwargs)
        context["featured_categories"] = (
            Category.objects.filter(is_active=True)
            .order_by("sort_order", "name")[:4]
        )
        context["latest_products"] = (
            Product.objects.filter(is_active=True)
            .order_by("-created_at")[:8]
        )
        context["hero_product"] = (
            Product.objects.filter(is_active=True, is_featured=True)
            .order_by("-created_at")
            .first()
        )
        return context


class CategoryDetailView(ListView):
    """Show products in a category with optional sorting and pagination."""

    model = Product
    template_name = "category.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):  # type: ignore[override]
        # Fetch the category or raise 404
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"], is_active=True)
        sort = self.request.GET.get("sort", "newest")
        qs = self.category.products.filter(is_active=True)
        if sort == "weight_desc":
            qs = qs.order_by("-weight_gram")
        elif sort == "weight_asc":
            qs = qs.order_by("weight_gram")
        else:
            qs = qs.order_by("-created_at")
        return qs

    def get_context_data(self, **kwargs):  # type: ignore[override]
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["current_sort"] = self.request.GET.get("sort", "newest")
        return context


class ProductDetailView(DetailView):
    """Display details of a single product and prepare a WhatsApp message."""

    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):  # type: ignore[override]
        return (
            super()
            .get_queryset()
            .filter(is_active=True)
            .select_related("category", "wage_tier")
            .prefetch_related("images")
        )

    def get_context_data(self, **kwargs):  # type: ignore[override]
        context = super().get_context_data(**kwargs)
        product = self.object
        if product.code:
            message = f"سلام، در مورد محصول {product.name} (کد: {product.code}) از سایت نور گلد می‌خواستم سوال بپرسم."
        else:
            message = f"سلام، در مورد محصول {product.name} از سایت نور گلد می‌خواستم سوال بپرسم."
        context["whatsapp_message"] = message
        return context


class ProductListView(ListView):
    """List all active products with pagination."""

    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):  # type: ignore[override]
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "wage_tier")
            .prefetch_related("images")
            .order_by("-created_at")
        )


# Function wrappers for backwards compatibility
home_view = HomeView.as_view()
category_detail_view = CategoryDetailView.as_view()
product_detail_view = ProductDetailView.as_view()
product_list_view = ProductListView.as_view()
