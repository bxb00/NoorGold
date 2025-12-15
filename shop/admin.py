from django.contrib import admin
from .models import Category, WageTier, Product, ProductImage, SiteConfig


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "is_main", "sort_order")
    verbose_name = "عکس محصول"
    verbose_name_plural = "عکس‌های محصول"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(WageTier)
class WageTierAdmin(admin.ModelAdmin):
    list_display = ("name", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "category",
        "wage_tier",
        "weight_gram",
        "is_active",
        "is_featured",
        "created_at",
    )
    list_filter = ("category", "wage_tier", "is_active", "is_featured")
    search_fields = ("name", "code")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("name", "code", "slug", "category", "wage_tier"),
        }),
        ("مشخصات محصول", {
            "fields": ("weight_gram", "description"),
        }),
        ("نمایش", {
            "fields": ("is_active", "is_featured"),
        }),
    )


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("store_name", "whatsapp_number", "phone_number", "updated_at")

    def has_add_permission(self, request):
        # Only allow one SiteConfig instance
        if SiteConfig.objects.exists():
            return False
        return super().has_add_permission(request)


# Admin site branding
admin.site.site_header = "پنل مدیریت نور گلد"
admin.site.site_title = "مدیریت نور گلد"
admin.site.index_title = "داشبورد مدیریت"