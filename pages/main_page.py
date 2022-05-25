from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_login_link(self):
        return self.is_element_present(By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
