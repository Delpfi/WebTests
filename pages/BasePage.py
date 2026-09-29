import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент на странице')
    def find_element(self,locator,time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}") #драйвер подожди макс. 5 сек до тех пор пока элемент не станет видимым, возвращает webelement

    @allure.step('Открываем страницу')
    def get_url(self,url):
        return self.driver.get(url)

    #функция что бы сделать скриншот, у allure есть функция attach
    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), 'скриншот', allure.attachment_type.PNG)