import time
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .constants import MAIN_PAGE_URL, LOGIN_PAGE_URL


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    assert page.should_be_login_link(), "Login link is not presented on the MainPage"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()
    tested_url = browser.current_url.split(sep='/')
    tested_url.pop(3)                                  # deleting language from url
    tested_url = '/'.join(tested_url)
    assert tested_url == LOGIN_PAGE_URL, f"Link to login page on the main page is broken:  {tested_url} != {LOGIN_PAGE_URL}"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.basket_is_empty(), 'Basket is no empty'


def test_guest_can_see_in_basket_opened_from_main_page_text_about_empty(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.guest_can_see_in_basket_opened_from_main_page_text_about_empty(), 'Guest can not see inscription ' \
                                                                                         'that bask is empty'
