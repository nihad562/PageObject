from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PAS_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_CONFIRMPAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
    MAIN_PRODUCT_TITLE = (By.CSS_SELECTOR, "div[class*='product_main'] h1")
    ADDED_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.alert:first-child strong")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*='product_main'] p.price_color")
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "a[href='/en-gb/accounts/']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, "span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
