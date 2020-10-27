import time
from selenium import webdriver


def test_page_contains_adding_to_cart_button(browser):
    try:
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        button = browser.find_element_by_xpath("// button[contains(text(), 'Добавить в корзину')]")
        assert button.is_displayed()


    finally:
        time.sleep(1)
        browser.quit()