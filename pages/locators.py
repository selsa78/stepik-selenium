from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link[href='/ru/accounts/login/']")
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')
    REGISTER_FORM = (By.CLASS_NAME, 'register_form')
    LOGIN_EMAIL = (By.NAME,'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Я забыл пароль')
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTRATION_EMAIL = (By.NAME,'registration-email')
    REGISTRATION_PASSWORD_1 = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_2 = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, 'h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    ALERT_ITEM_NAME = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    ALERT_ITEM_PRICE = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')