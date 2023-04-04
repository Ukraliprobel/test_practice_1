from selenium.common.exceptions import NoSuchElementException #имя исключения

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   #в конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):   #в нем будем перехватывать исключение с аргментами как искать(css, id, xpath и тд) и что искать(строку-селектор)
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException: #имя исключения
            return False
        return True
