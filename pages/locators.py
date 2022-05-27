from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_PRODUCT_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    EXPECTED_PRODUCT = (By.CSS_SELECTOR, '.alertinner strong')
    EXPECTED_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".alert-success")
