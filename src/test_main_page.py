import pytest

from .pages.base_page import BasePage

# def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    login_page = page.go_to_login_page()
#    login_page.should_be_login_page()


# def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()
#
# def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = MainPage(browser, link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.solve_quiz_and_get_code()
    expected_text = page.get_main_product_title()
    expected_price = page.get_main_product_price()
    page.should_display_message_with_expected_text_when_add_product(expected_text)
    page.should_display_message_with_expected_price_when_add_product(expected_price)



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    product_page = MainPage(browser, link)
    product_page.open()
    basket_page = BasketPage(browser)
    basket_page.should_have_empty_basket()
    basket_page.should_contain_text_in_empty_basket_message('Your basket is empty')