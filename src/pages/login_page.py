from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PAS_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONFIRMPAS_FIELD).send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "button[name='registration_submit']").click()


