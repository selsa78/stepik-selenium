from .base_page import BasePage


class MainPage(BasePage): 
    #Поставили заглушку, т.к. все вынесли в BasePage и locators
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    #Можно еще короче
    # class MainPage(BasePage):
    #pass    