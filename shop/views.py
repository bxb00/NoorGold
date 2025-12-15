# shop/views.py
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def home_view(request):
    """
    Home page: hero, featured categories, latest products.
    """
    featured_categories = Category.objects.filter(is_active=True).order_by("sort_order", "name")[:4]
    latest_products = Product.objects.filter(is_active=True).order_by("-created_at")[:8]

    hero_product = (
        Product.objects.filter(is_active=True, is_featured=True)
        .order_by("-created_at")
        .first()
    )

    context = {
        "featured_categories": featured_categories,
        "latest_products": latest_products,
        "hero_product": hero_product,
    }
    return render(request, "home.html", context)


def category_detail_view(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)

    sort = request.GET.get("sort", "newest")
    qs = category.products.filter(is_active=True)

    if sort == "weight_desc":
        products = qs.order_by("-weight_gram")
    elif sort == "weight_asc":
        products = qs.order_by("weight_gram")
    else:  # newest
        products = qs.order_by("-created_at")

    context = {
        "category": category,
        "products": products,
        "current_sort": sort,
    }
    return render(request, "category.html", context)





def product_detail_view(request, slug):
    """
    Product detail page: show one product and its images.
    """
    product = get_object_or_404(
        Product.objects.select_related("category", "wage_tier").prefetch_related("images"),
        slug=slug,
        is_active=True,
    )

    # Build WhatsApp message text (in Persian)
    if product.code:
        whatsapp_message = f"سلام، در مورد محصول {product.name} (کد: {product.code}) از سایت نور گلد می‌خواستم سوال بپرسم."
    else:
        whatsapp_message = f"سلام، در مورد محصول {product.name} از سایت نور گلد می‌خواستم سوال بپرسم."

    context = {
        "product": product,
        "whatsapp_message": whatsapp_message,
    }
    return render(request, "product_detail.html", context)

def product_list_view(request):
    products = (
        Product.objects.filter(is_active=True)
        .select_related("category", "wage_tier")
        .prefetch_related("images")
        .order_by("-created_at")
    )
    context = {"products": products}
    return render(request, "product_list.html", context)