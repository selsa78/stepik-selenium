import math
from .locators import BasePageLocators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import Exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException



class BasePage():
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        #def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout) #- закомменчено т.к. ждем появления элемента явно
    
    def go_to_login_page(self):
        #link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID) # неверный линк для проверки
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,"                                                                  " probably unauthorised user"
    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"   
        
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"   
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4): #Резюмируя, можно сказать, что разрабатывать такие проверки нужно очень аккуратно, использовать явные ожидания для сокращения времени прогона теста и всегда добавлять позитивную проверку на элемент в другом тесте. Без явной необходимости таких проверок лучше избегать. 
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
 
    def is_disappeared(self, how, what, timeout=4): #Резюмируя, можно сказать, что разрабатывать такие проверки нужно очень аккуратно, использовать явные ожидания для сокращения времени прогона теста и всегда добавлять позитивную проверку на элемент в другом тесте. Без явной необходимости таких проверок лучше избегать. 
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
 
    
    def open(self):
        self.browser.get(self.url)
        
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
