from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PAS_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_CONFIRMPAS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[class*='add-to-basket']")