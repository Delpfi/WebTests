from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class HelpPageLocators():
    SEARCH_FIELD = (By.XPATH, '//*[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//*[@name="illustrations/ill_actual"]')
    REGISTRATION = (By.XPATH, '//*[@href="/help/registraciya"]')
    MY_PROFILE = (By.XPATH, '//*[@href="/help/moi-profil"]')
    COMMUNICATION = (By.XPATH, '//*[@href="/help/obshchenie"]')
    PROFILE_ACCESS = (By.XPATH, '//*[@href="/help/dostup-k-profilu"]')
    SECURITY = (By.XPATH, '//*[@href="/help/bezopasnost"]')
    GROUPS = (By.XPATH, '//*[@href="/help/gruppy"]')
    PAYED_FUNCTIONS = (By.XPATH, '//*[@href="/help/platnye-funkcii"]')
    SPAM = (By.XPATH, '//*[@href="/help/narusheniya-i-spam"]')
    GAMES_AND_APPS = (By.XPATH, '//*[@name="illustrations/ill_app_game"]')
    OTHER_SERVICES = (By.XPATH, '//*[@name="illustrations/ill_other_services"]')
    IMPORTANT_INFORMATION = (By.XPATH, '//*[@name="illustrations/ill_useful_info"]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//*[@name="illustrations/ill_advertising_cabinet"]')

class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)


    def scrollToitem(self,locator):
        with allure.step('Скролл к нужному элементу'):
            scroll_item = self.find_element(locator)#элемент до которого нужно до скролить
            ActionChains(self.driver).scroll_to_element(scroll_item).perform()
            self.attach_screenshot()
            ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform() # perform() обязательная функция, без нее не выполниться действия
