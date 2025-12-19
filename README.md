# NoorGold

NoorGold is a modern and responsive web application for managing and displaying a jewellery catalogue.  
It is built with **Django 4** on the back‑end and **Bootstrap 5 RTL** on the front‑end to provide a polished user experience in Persian (Farsi) for right‑to‑left (RTL) layouts.  
The project includes custom models for categories, products, wage tiers, product images and site configuration, with automatic slug generation and pagination for product lists.

## Features

* **Responsive design** – Uses Bootstrap 5 with RTL support to ensure pages look great on desktops, tablets and phones.
* **Category & product management** – Models for categories (`Category`) and products (`Product`) with related wage tiers and images. Each product may have multiple images and can be marked as **featured**.
* **Automatic slug generation** – Category and product names are converted to URL‑friendly slugs automatically; duplicates are avoided by appending numbers when necessary.
* **Pagination & sorting** – Product lists and category pages support pagination and optional sorting by newest, highest weight or lowest weight.
* **Admin interface** – Leverages Django’s admin site for CRUD operations on categories, products, wage tiers and site configuration.
* **Site configuration** – A single `SiteConfig` object stores global settings such as the WhatsApp number and the hero product for the home page.
* **SEO meta tags** – The base template includes meta tags for description and keywords to improve search engine optimisation.

## Quickstart

The following steps will get a copy of the project running on your local machine for development and testing purposes. These commands assume a Unix‑like environment; adjust paths for Windows as necessary.

### Prerequisites

* Python 3.9 or newer
* `pip` and virtual environment tools (`venv` or `virtualenv`)
* [Git](https://git-scm.com/) to clone the repository

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/bxb00/NoorGold.git
   cd NoorGold
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If the project does not yet include a `requirements.txt`, install Django manually:

   ```bash
   pip install django==4.0.*
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional but recommended)**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an administrative account.

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   You can now access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and the admin site at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Usage

### Adding categories, products and images

1. Log in to the admin site with the superuser credentials you created.
2. Add one or more **wage tiers**; these define pricing categories (e.g. *Normal*, *Low*, etc.).
3. Create **categories** for different product types, such as rings, bracelets or necklaces.
4. When adding a **product**, choose its category and wage tier, specify the approximate weight (gram), and optionally add a description and mark it as featured.
5. After saving the product, you can upload multiple **images** in the *Product images* section. The first image becomes the main product image on listing pages and the product detail page.

### Site configuration

The `SiteConfig` model holds global settings for your shop. You can manage it via the admin site:

* **Hero product** – Select a product to feature prominently on the home page.
* **WhatsApp number** – Provide a number so that visitors can click a button to start a WhatsApp conversation about a product.
* You can extend the `SiteConfig` model with additional fields (e.g. contact email, address) as needed.

### Customising styles

All custom CSS rules have been moved to `static/css/styles.css` to promote clean templates and enable browser caching.  
If you want to adjust colours, fonts or layouts, edit this file. Variables such as `--gold` and `--bg-main` at the top of the file control the main palette.

JavaScript that powers the product detail page thumbnails lives in `static/js/product_detail.js`.

## Project structure

```
NoorGold/
├── manage.py         # Django’s command-line utility
├── noorGold/         # Project configuration (settings, urls, wsgi)
├── shop/             # Main application: models, views, URL routing
│   ├── models.py     # Category, WageTier, Product, ProductImage, SiteConfig
│   ├── views.py      # Class-based views for pages
│   ├── urls.py       # URL patterns for the shop app
│   └── context_processors.py # Injects categories and site config into templates
├── templates/        # HTML templates for pages (home, category, product)
├── static/           # Static assets (CSS and JavaScript)
│   ├── css/styles.css
│   └── js/product_detail.js
└── README.md         # Project documentation (you are reading it now)
```

## Contributing

Pull requests are welcome! To contribute:

1. Fork the repository and create a new branch (e.g. `feature/your-feature`).
2. Make your changes following the [Django coding style guide](https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/#coding-style).
3. Write or update tests if applicable, and ensure all tests pass.
4. Submit a pull request explaining the motivation for your changes.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.  
If the repository does not include a license file, please add one or choose a licence appropriate for your organisation.

## Acknowledgements

* This project is inspired by the need for an RTL‑friendly e‑commerce platform for jewellery shops.
* Icons are provided by [Bootstrap Icons](https://icons.getbootstrap.com/).
* Built with love using Django and Bootstrap.
