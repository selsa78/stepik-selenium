import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_proper_item()
        
            
    def should_be_proper_item(self):
        itemtext = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        addeditemtext = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert addeditemtext == itemtext, "Wrong item added to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


    def should_success_message_diasppeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
 
    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to cart link is not presented"
    
    def click_add_to_basket(self):
        AddButton = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        AddButton.click()
 
      

