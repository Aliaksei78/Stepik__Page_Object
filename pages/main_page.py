from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_login_link(self):
        return self.is_element_present(*MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
