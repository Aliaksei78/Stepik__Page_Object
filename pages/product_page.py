from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_FOR_ADD_TO_BASKET)
        product = product.text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_FOR_ADD_TO_BASKET)
        price = price.text
        expected_product = self.browser.find_element(*ProductPageLocators.EXPECTED_PRODUCT)
        expected_product = expected_product.text
        expected_price = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE)
        expected_price = expected_price.text
        return product, price, expected_product, expected_price
