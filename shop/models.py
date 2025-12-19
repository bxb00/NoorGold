"""
Database models for the shop application.

This module defines core entities such as categories, wage tiers, products and
their related images. Enhancements include automatic slug generation and
validation to ensure clean URLs and positive weights.
"""

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class Category(models.Model):
    """A group of products such as rings, necklaces or bracelets."""

    name = models.CharField(max_length=100, verbose_name="نام دسته")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="اسلاگ")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["sort_order", "name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name

    def save(self, *args, **kwargs) -> None:
        """Automatically generate a unique slug from the name if none is set."""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            idx = 1
            # Ensure uniqueness by appending a numeric suffix if necessary
            while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{idx}"
                idx += 1
            self.slug = slug
        super().save(*args, **kwargs)


class WageTier(models.Model):
    """Represents a pricing tier for labor cost (اجرت)."""

    name = models.CharField(max_length=50, verbose_name="نام اجرت")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیحات")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "نوع اجرت"
        verbose_name_plural = "انواع اجرت"
        ordering = ["sort_order", "name"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name


class Product(models.Model):
    """A purchasable item in the shop with optional images and metadata."""

    name = models.CharField(max_length=150, verbose_name="نام محصول")
    code = models.CharField(max_length=50, blank=True, verbose_name="کد محصول")
    slug = models.SlugField(max_length=180, unique=True, verbose_name="اسلاگ")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="دسته‌بندی",
    )
    wage_tier = models.ForeignKey(
        WageTier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="نوع اجرت",
    )
    weight_gram = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="وزن (گرم)",
    )
    description = models.TextField(blank=True, verbose_name="توضیحات")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_featured = models.BooleanField(
        default=False,
        verbose_name="نمایش ویژه در صفحه اصلی",
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاریخ ایجاد",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name

    def save(self, *args, **kwargs) -> None:
        """Automatically generate a unique slug from the product name if none is set."""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            idx = 1
            # Ensure uniqueness by appending a numeric suffix if necessary
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{idx}"
                idx += 1
            self.slug = slug
        super().save(*args, **kwargs)


def product_image_upload_path(instance: "ProductImage", filename: str) -> str:
    """Compute upload path for product images: media/products/<product_id>/<filename>"""
    return f"products/{instance.product_id}/{filename}"


class ProductImage(models.Model):
    """An image associated with a product."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول",
    )
    image = models.ImageField(
        upload_to=product_image_upload_path,
        verbose_name="عکس",
    )
    is_main = models.BooleanField(default=False, verbose_name="عکس اصلی")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")

    class Meta:
        verbose_name = "عکس محصول"
        verbose_name_plural = "عکس‌های محصول"
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"عکس {self.product.name}"


class SiteConfig(models.Model):
    """Singleton configuration model storing global site information."""

    whatsapp_number = models.CharField(
        max_length=20,
        verbose_name="شماره واتساپ (بدون صفر، با 98)",
    )
    store_name = models.CharField(
        max_length=150,
        default="نور گلد",
        verbose_name="نام فروشگاه",
    )
    address = models.TextField(blank=True, verbose_name="آدرس")
    instagram_link = models.URLField(blank=True, verbose_name="لینک اینستاگرام")
    phone_number = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="شماره تماس",
    )
    working_hours = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="ساعات کاری",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return "تنظیمات سایت"
