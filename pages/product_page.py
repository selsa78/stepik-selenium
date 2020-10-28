from .base_page import BasePage
from .locators import ProductPageLocators

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def match_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME).text
        assert item_name == alert_item_name

    def match_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        alert_item_price = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_PRICE).text
        assert item_price == alert_item_price
