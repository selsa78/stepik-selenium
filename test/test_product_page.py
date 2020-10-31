import time, pytest
from pages.product_page import ProductPage # иногда в начале нужна точка
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#browser.delete_all_cookies()  # очистка кукисов
####urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.need_review
#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket(browser):
    itempage = ProductPage(browser, link)
    itempage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину(мы только вошли на страницу)
    itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    itempage.click_add_to_basket() #Нажимаем добавить в корзину
    itempage.solve_quiz_and_get_code()  # Нужен алерт для этого метода - решаем, вставляем значение 
    itempage.should_be_proper_item() # проверяем что в корзину добавлен правильный товар
  
  
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):    
    itempage = ProductPage(browser, link)
    itempage.open() #Открываем страницу товара
    itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    itempage.click_add_to_basket() #Наживаем добавить в корзину
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе   
    
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):    
    itempage = ProductPage(browser, link)
    itempage.open()  #Открываем страницу товара
    itempage.should_not_be_success_message() # Проверяем, есть ли сообщение об успехе 
      
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):    
    itempage = ProductPage(browser, link)
    itempage.open()  #Открываем страницу товара
    itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
    itempage.click_add_to_basket() #Наживаем добавить в корзину
    itempage.should_success_message_diasppeared() # Проверяем, исчезло ли сообщение об успехе

      
@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.skip   # из предыдущего задания  
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(10)
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.need_review
#@pytest.mark.skip   # из предыдущего задания  
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    basketpage=BasketPage(browser, link)
    basketpage.open()
    basketpage.should_be_basket_link()
    basketpage.go_to_basket_page()
    basketpage.should_be_no_items_in_basket()
    #time.sleep(5)


@pytest.mark.skip   # проверка регистрации
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_see_login_page(browser, link):
    EMAIL = str(time.time()) + "@fakemail.org"
    PASSWORD= "1qaz2wsx3edc_"
    loginpage=LoginPage(browser, link)
    loginpage.open()
    loginpage.should_be_login_link()
    loginpage.go_to_login_page()
    loginpage.should_be_login_page()
    loginpage.should_be_register_button()
    loginpage.register_new_user(EMAIL,PASSWORD)
    loginpage.click_register_button()
    loginpage.should_be_authorized_user()
        

class TestUserAddToBasketFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True) # scope="class" "function"
    def setup(self, browser):
        EMAIL = str(time.time()) + "@fakemail.org"
        PASSWORD= "1qaz2wsx3edc_"
        loginpage = LoginPage(browser, link)
        loginpage.open()
        loginpage.should_be_login_link()
        loginpage.go_to_login_page()
        loginpage.should_be_login_page()
        loginpage.should_be_register_button()
        loginpage.register_new_user(EMAIL,PASSWORD)
        loginpage.click_register_button()
        loginpage.should_be_authorized_user()
        
    
    def test_user_cant_see_success_message(self, browser):    
        itempage = ProductPage(browser, link)
        itempage.open() #Открываем страницу товара
        #time.sleep(10)
        itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину в самом начале
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        itempage = ProductPage(browser, link)
        itempage.open()  #Открываем страницу товара
        itempage.should_not_be_success_message() # проверяем что нет сообщения о добавлении в корзину в самом начале
        itempage.should_be_add_to_basket_link() # Есть кнопка добавить в корзину
        itempage.click_add_to_basket() #Нажимаем добавить в корзину
        itempage.solve_quiz_and_get_code()  # решаем, вставляем значение 
        itempage.should_be_proper_item() # проверяем что в корзину добавлен правильный товар
