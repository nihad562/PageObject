from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_have_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "The basket should be empty"

    def should_contain_text_in_empty_basket_message(self, expected_text):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert expected_text in empty_basket_message, "Message for empty basket should have expected text"