import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser)
    basket_page.should_have_empty_basket()
    basket_page.should_contain_text_in_empty_basket_message('Your basket is empty')


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.solve_quiz_and_get_code()
    expected_text = page.get_main_product_title()
    expected_price = page.get_main_product_price()
    page.should_display_message_with_expected_text_when_add_product(expected_text)
    page.should_display_message_with_expected_price_when_add_product(expected_price)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.go_to_login_page()
        page.register_new_user("хуйевгеньевич", "мускул")
        page.user_should_be_logged_in()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.solve_quiz_and_get_code()
        expected_text = page.get_added_to_basket_product_title()
        expected_price = page.get_added_to_basket_product_price()
        page.should_display_message_with_expected_text_when_add_product(expected_text)
        page.should_display_message_with_expected_price_when_add_product(expected_price)
