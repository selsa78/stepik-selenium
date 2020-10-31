from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD1 = (By.NAME, "registration-password1")
    PASSWORD2 = (By.NAME, "registration-password2")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a.btn-default") # ".basket-mini .btn-group a.btn-default"
    EMPTY_BASKET_TAG = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET_TAG = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")