from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_GO_TO_BASKET_PAGE = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_pod button')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FIELD = (By.NAME, 'registration-email')
    REGISTER_PASSWORD_FIELD = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.NAME, 'registration-password2')
    BTN_REGISTER = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRICE_PRODUCT_FOR_ADD_TO_BASKET = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    EXPECTED_PRODUCT = (By.CSS_SELECTOR, '.alertinner strong')
    EXPECTED_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    TEXT_BASKET_IS_NO_EMPTY = (By.CLASS_NAME, 'total')
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')

