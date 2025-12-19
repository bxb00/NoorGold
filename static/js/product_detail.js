/*
 * Product detail interactions.
 *
 * This script enables thumbnail clicking to update the main product image
 * on the product detail page. It is loaded in the `extra_scripts` block
 * of ``product_detail.html``.
 */

document.addEventListener('DOMContentLoaded', () => {
    const mainImg = document.querySelector('[data-main-product-image]');
    const thumbs = document.querySelectorAll('[data-thumb-image]');

    if (mainImg && thumbs.length) {
        thumbs.forEach(thumb => {
            thumb.addEventListener('click', () => {
                const src = thumb.getAttribute('data-full-src');
                if (src) {
                    mainImg.setAttribute('src', src);
                }
            });
        });
    }
});
