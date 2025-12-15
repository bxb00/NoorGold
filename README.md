# Noor Gold – Jewelry Catalog (Django)

Noor Gold is a simple, elegant jewelry catalog website for a physical gold/jewelry shop.  
The site is fully **Persian (RTL)** and focuses on:

- Showing products (bracelets, necklaces, rings, sets, etc.)
- Managing products and categories through an admin panel
- Letting customers contact the shop via **WhatsApp** for price and ordering

There is **no online payment** in this project – all deals are finalized over WhatsApp.

---

## Tech Stack

- **Backend:** Django 4.x
- **Database:** SQLite (development / simple deployments)
- **Frontend:** Django templates + Bootstrap 5 (RTL) + custom CSS
- **Images:** Django `ImageField` with `Pillow`
- **Docker:** Optional, for local development / quick run

---

## Main Features

- Fully **RTL** and **Persian UI** (front & admin)
- Categories (e.g. rings, bracelets, necklaces, full sets, etc.)
- Dynamic product listing:
  - Category pages
  - "Latest products" on the home page
  - Featured product section in the hero
- Product details:
  - Multiple images per product
  - Weight (grams)
  - Wage tier (economic / medium / luxury / …)
  - Description
  - One-click WhatsApp link with pre-filled message
- Admin panel (Django admin) customized in Persian:
  - Manage categories
  - Manage wage tiers
  - Manage products & product images
  - Manage basic site config (store name, address, phone, WhatsApp number, Instagram link)

---

## Project Structure

```text
noor-gold/
  manage.py
  noor_gold/
    settings.py
    urls.py
    wsgi.py
  shop/
    models.py          # Category, WageTier, Product, ProductImage, SiteConfig
    views.py           # Home, category list, product detail, product list
    admin.py           # Persian-friendly admin configuration
    context_processors.py  # navbar categories + site config
    urls.py
  templates/
    base.html
    home.html
    category.html
    product_detail.html
    product_list.html
  media/               # uploaded product images (ignored by git)
  requirements.txt
  Dockerfile