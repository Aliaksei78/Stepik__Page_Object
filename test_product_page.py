import time
import pytest
from .pages.product_page import ProductPage
from .constants import PRODUCT_PAGE_URL, LOGIN_PAGE_URL
# from .locators import ProductPageLocators


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail(reason="We will not fix it!!!")),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_right_product(browser, link):
    # page = ProductPage(browser, PRODUCT_PAGE_URL)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.product == page.expected_product, f"The product  '{page.expected_product}' in the basket" \
                                                  f" not equal the chosen '{page.product}'"


# А можно и так спарамертизировать, то же самое, но гораздо компактнее
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail(reason="We will not fix it!!!")),
                                         "8", "9"])
def test_guest_can_add_product_to_basket_right_price(browser, promo_offer):
    # page = ProductPage(browser, PRODUCT_PAGE_URL)
    page = ProductPage(browser,
                       f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}")
    page.open()
    page.add_product_to_basket()
    assert page.price == page.expected_price, f"The price  '{page.expected_price}' in the basket" \
                                              f" not equal the chosen '{page.price}'"


@pytest.mark.skip(reason='This test was born to fall')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_success_message_present(), 'Success message is presented but should not be'


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    assert page.is_not_success_message_present(), 'Success message is presented but should not be'


@pytest.mark.xfail(reason='It was a strange idea from the first second')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared_success_message(), 'The success message is not disappeared but it OK'


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    assert page.should_be_login_link(), "Login link is not presented on the ProductPage"


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.go_to_login_page()
    tested_url = browser.current_url.split(sep='/')
    tested_url.pop(3)  # deleting language from url
    tested_url = '/'.join(tested_url)
    assert tested_url == LOGIN_PAGE_URL, f"Link to login page on the main page is broken:  {tested_url} != {LOGIN_PAGE_URL}"
