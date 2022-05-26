from .pages.login_page import LoginPage
from .constants import LOGIN_PAGE_URL


def test_should_be_login_url(browser):
    page = LoginPage(browser, LOGIN_PAGE_URL)
    page.open()
    login_url = page.should_be_login_url()
    login_url = login_url.split(sep='/')
    login_url.pop(3)                                # deleting language from url
    login_url = '/'.join(login_url)
    assert login_url == LOGIN_PAGE_URL, f"Link to login page on main page is broken:  {login_url} != {LOGIN_PAGE_URL}"
    # Такая реализация лучше предлагаемой на курсе, т.к. полностью проверяет ссылку, а не только слово login.


def test_should_be_login_form(browser):
    page = LoginPage(browser, LOGIN_PAGE_URL)
    page.open()
    assert page.should_be_login_form(), "Login form is not detected"


def test_should_be_register_form(browser):
    page = LoginPage(browser, LOGIN_PAGE_URL)
    page.open()
    assert page.should_be_register_form(), 'Register form is not detected'
