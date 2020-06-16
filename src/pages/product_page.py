from selenium.common.exceptions import NoAlertPresentException

from src.pages.base_page import BasePage
from src.pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
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
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_TITLE).text

    def get_added_to_basket_product_title(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_TITLE).text

    def get_main_product_price(self):
        return self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRICE).text

    def get_added_to_basket_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_PRICE).text
