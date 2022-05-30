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

    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        field_email.clear()
        field_email.send_keys(email)

        field_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        field_password.clear()
        field_password.send_keys(password)

        field_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_FIELD)
        field_password_confirm.clear()
        field_password_confirm.send_keys(password)

        btn_register = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
        btn_register.click()


