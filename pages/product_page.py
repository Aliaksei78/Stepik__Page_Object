from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=5):
        BasePage.__init__(self, browser, url, timeout)
        self.product = None
        self.price = None
        self.expected_product = None
        self.expected_price = None
        self.success_message = None

    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_FOR_ADD_TO_BASKET)
        self.product = product.text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_FOR_ADD_TO_BASKET)
        self.price = price.text
        expected_product = self.browser.find_element(*ProductPageLocators.EXPECTED_PRODUCT)
        self.expected_product = expected_product.text
        expected_price = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE)
        self.expected_price = expected_price.text
        self.success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MASSAGE)

    def is_not_success_message_present(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MASSAGE)

    def is_disappeared_success_message(self):
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE)
