import allure

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
    RECOVER_LINK_BUTTON = (By.ID, 'lockout-recover-btn')
    GO_BACK_BUTTON = (By.ID,'lockout-cancel-btn')
    REGISTER_BUTTON = (By.ID, 'lockout-register-btn')
    REGISTRATION_BUTTON = (By.ID, 'hero-register-btn')


class LoginPageHelper(BasePage): #при создании объекта данного класса проверка будет автоматически
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.TAB_LOGIN)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()  #find_element - возвращает объект класс webelement

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.TEXT_LOGIN_ERROR).text

    @allure.step('Заполняем поле логин')
    def type_login(self,text_login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def type_password(self, text_password):
        self.find_element(LoginPageLocators.LOGIN_PASSWORD).send_keys(text_password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVER_LINK_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
        self.attach_screenshot()