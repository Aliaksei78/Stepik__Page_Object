from .pages.product_page import ProductPage
from .constants import PRODUCT_PAGE_URL


def test_guest_can_add_product_to_basket_right_product(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    product, price, expected_product, expected_price = page.add_product_to_basket()
    assert product == expected_product, f"The product  '{expected_product}' in the basket not equal the chosen '{product}'"


def test_guest_can_add_product_to_basket_right_price(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    product, price, expected_product, expected_price = page.add_product_to_basket()
    assert price == expected_price, f"The price  '{expected_price}' in the basket not equal the chosen '{price}'"
