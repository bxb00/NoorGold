"""
Context processors for the shop app.

Provides global variables used throughout templates such as the list of
categories to populate the navigation bar and the site configuration.
"""

from .models import Category, SiteConfig


def global_context(request):  # pragma: no cover - simple context provider
    """Global context for navbar categories and site configuration.

    This makes categories and site configuration available in every template.
    """
    navbar_categories = Category.objects.filter(is_active=True).order_by("sort_order", "name")
    site_config = SiteConfig.objects.first()
    return {
        "navbar_categories": navbar_categories,
        "site_config": site_config,
    }
