from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators():
    #локатары для - https://sn.rv-school.ru/
    LOGIN_FIELD = (By.ID, 'login-phone-email')
    LOGIN_PASSWORD = (By.ID, 'login-password')
    LOGIN_BUTTON = (By.XPATH, '//*[@class="login-submit"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@class="forgot-link"]')
    QR_BUTTON = (By.ID, 'tabQr')
    TAB_LOGIN = (By.ID, 'tabLogin')
    TEXT_LOGIN_ERROR = (By.ID, 'login-error')



class LoginPageHelper(BasePage): #при создании объекта данного класса проверка будет автоматически
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.TAB_LOGIN)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()  #find_element - возвращает объект класс webelement

    def get_error_text(self):
        return self.find_element(LoginPageLocators.TEXT_LOGIN_ERROR).text

    def send_keys_text(self,text_login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_login)

