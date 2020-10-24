

class BasePage():
    def __init__(self, browser, url): # конструктор — метод, который вызывается, когда мы создаем объект.
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)