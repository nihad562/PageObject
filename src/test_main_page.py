from .pages.base_page import BasePage


#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    login_page = page.go_to_login_page()
#    login_page.should_be_login_page()


#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()
#
#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = MainPage(browser, link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()

def test_code(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
    page = BasePage(browser, link)
    page.open()
    page.solve_quiz_and_get_code()
    print()