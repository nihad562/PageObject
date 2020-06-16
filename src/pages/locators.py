from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PAS_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_CONFIRMPAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    #GoodPage
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[class*='add-to-basket']")
    MAIN_PRODUCT_TITLE = (By.CSS_SELECTOR, "div[class*='product_main'] h1")
    ADDED_TO_BASKET_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.alert:first-child strong")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*='product_main'] p.price_color")
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) strong")