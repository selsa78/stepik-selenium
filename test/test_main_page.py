import time, pytest
from pages.main_page import MainPage # иногда в начале нужна точка
from pages.login_page import LoginPage # иногда в начале нужна точка
from pages.basket_page import BasketPage


#@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" #Рабочий линк
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page.should_be_login_link()      # проверяем наличие ссылки на вход
    page.should_be_login_page()            # проверям наличи формы логин-регистрация

 
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    basketpage = BasketPage(browser, link)
    basketpage.open()
    basketpage.should_be_basket_link()
    basketpage.go_to_basket_page()
    basketpage.should_be_no_items_in_basket()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
    def test_guest_can_go_to_login_page(self, browser, link):     
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        page.should_be_login_link()      # проверяем наличие ссылки на вход
        page.should_be_login_page()            # проверям наличи формы логин-регистрация

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
    def test_guest_should_see_login_link(self, browser,link):
        page = MainPage(browser, link)
        page.open()
        #time.sleep(5)
        page.should_be_login_link()
        