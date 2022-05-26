import pytest
from .pages.product_page import ProductPage
from .constants import PRODUCT_PAGE_URL


# @pytest.mark.parametrize('link',
#                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                           pytest.param(
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                               marks=pytest.mark.xfail(reason="We will not fix it!!!")),
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket_right_product(browser, link):
#     # page = ProductPage(browser, PRODUCT_PAGE_URL)
#     page = ProductPage(browser, link)
#     page.open()
#     product, price, expected_product, expected_price = page.add_product_to_basket()
#     assert product == expected_product, f"The product  '{expected_product}' in the basket not equal the chosen '{product}'"


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail(reason="We will not fix it!!!")), "8", "9"])
def test_guest_can_add_product_to_basket_right_price(browser, promo_offer):
    # page = ProductPage(browser, PRODUCT_PAGE_URL)
    page = ProductPage(browser, f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}")
    page.open()
    product, price, expected_product, expected_price = page.add_product_to_basket()
    assert price == expected_price, f"The price  '{expected_price}' in the basket not equal the chosen '{price}'"
