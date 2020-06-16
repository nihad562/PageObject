import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

from .locators import LoginPageLocators


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        btn = self.browser.find_element(*LoginPageLocators.ADD_TO_BASKET)
        btn.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_main_product_title(self):
        return self.browser.find_element(*LoginPageLocators.MAIN_PRODUCT_TITLE).text

    def get_added_to_basket_product_title(self):
        return self.browser.find_element(*LoginPageLocators.ADDED_TO_BASKET_PRODUCT_TITLE).text

    def get_main_product_price(self):
        return self.browser.find_element(*LoginPageLocators.MAIN_PRODUCT_PRICE).text

    def get_added_to_basket_product_price(self):
        return self.browser.find_element(*LoginPageLocators.ADDED_TO_BASKET_PRODUCT_PRICE).text
