from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators():
    REGISTRATION_BY_PHONE_BUTTON = (By.ID, 'register-phone-toggle')

    PHONE_FIELD = (By.ID, 'phone-number-input')
    CONTRY_LIST = (By.ID, 'phone-country-select')
    CONTRY_ITEM = (By.XPATH, '//*[@id="phone-country-select"]/option')
    SEND_CODE_BUTTON = (By.ID, 'phone-send-code-btn')
    REGISTRATION_BY_EMAIL_CANCEL_BUTTON = (By.ID, 'phone-cancel-btn')
    BUTTON_LOGIN = (By.ID, 'login-link-anchor')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.click_next_page_registration_phone()
        self.check_page_by_phone()


    def click_next_page_registration_phone(self):
        with allure.step('Перейти на страницу регистрации по телефону'):
            self.find_element(RegistrationPageLocators.REGISTRATION_BY_PHONE_BUTTON).click()
            self.attach_screenshot()

    def check_page_by_phone(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.CONTRY_LIST)
            self.find_element(RegistrationPageLocators.SEND_CODE_BUTTON)
            self.find_element(RegistrationPageLocators.REGISTRATION_BY_EMAIL_CANCEL_BUTTON)
            self.find_element(RegistrationPageLocators.BUTTON_LOGIN)


    def select_random_country(self):
        with allure.step('Выбрать рандомно из выпадающего списка страну и код'):
            random_number = random.randint(0, 39)
            self.find_element(RegistrationPageLocators.CONTRY_LIST).click()
            country_items =  self.find_elements(RegistrationPageLocators.CONTRY_ITEM)
            country_items[random_number].click()
            self.attach_screenshot()
        return country_items[random_number].text


    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.CONTRY_LIST).get_attribute('value') #после того как выбрали рандомную страну т.е на нее нажали, определяем код у атрибута value