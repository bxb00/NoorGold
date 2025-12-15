# shop/context_processors.py
from .models import Category, SiteConfig


def global_context(request):
    """
    Global context for navbar categories and site configuration.
    """
    navbar_categories = Category.objects.filter(is_active=True).order_by("sort_order", "name")

    site_config = SiteConfig.objects.first()  # we only allow one config instance

    return {
        "navbar_categories": navbar_categories,
        "site_config": site_config,
    }