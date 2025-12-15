from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="اسلاگ")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class WageTier(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام اجرت")
    description = models.CharField(max_length=255, blank=True, verbose_name="توضیحات")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "نوع اجرت"
        verbose_name_plural = "انواع اجرت"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class Product(models.Model):
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

    def __str__(self):
        return self.name


def product_image_upload_path(instance, filename: str) -> str:
    # Upload path: media/products/<product_id>/<filename>
    return f"products/{instance.product_id}/{filename}"


class ProductImage(models.Model):
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

    def __str__(self):
        return f"عکس {self.product.name}"


class SiteConfig(models.Model):
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

    def __str__(self):
        return "تنظیمات سایت"