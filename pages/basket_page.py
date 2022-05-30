from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import BasketPageLocators
from .languages import languages


class BasketPage(BasePage):
    def basket_is_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_NO_EMPTY)
        except NoSuchElementException:
            return True
        return False

    def guest_can_see_in_basket_opened_from_main_page_text_about_empty(self):
        try:
            text_about_empty = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY)
            text_about_empty = text_about_empty.text
            for x in languages:
                if x in text_about_empty:
                    return True
            else:
                return False
        except NoSuchElementException:
            return False
