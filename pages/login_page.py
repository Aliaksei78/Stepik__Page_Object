"""
Предлагаемый курсом вариант:
                            class LoginPage(BasePage):
                                def should_be_login_url(self):
                                    # реализуйте проверку на корректный url адрес
                                    assert True

                                def should_be_login_form(self):
                                    # реализуйте проверку, что есть форма логина
                                    assert True

                                def should_be_register_form(self):
                                    # реализуйте проверку, что есть форма регистрации на странице
                                    assert True
не соответсвует сути Page Object, т.е. так делать, конечно, можно, но это уже не Page Object. т.к. asserts должны
быть в тестах, а не в страницах. Сделал правильно. Вроде))
"""

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        return self.browser.current_url

    def should_be_login_form(self):
        return self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        return self.is_element_present(*LoginPageLocators.REGISTER_FORM)
