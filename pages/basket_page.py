import time, pytest
from .base_page import BasePage
from .locators import BasePageLocators



class BasketPage(BasePage):
   
    def should_be_no_items_in_basket(self):
        EmptyBasketText = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_TAG).text
        assert "Your basket is empty" in EmptyBasketText, "Basket is not empty"
        assert self.is_not_element_present(*BasePageLocators.NOT_EMPTY_BASKET_TAG), "Not empty Basket tag present" 
