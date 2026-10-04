from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class RecoveryPageLocators():
    PHONE_BUTTON = (By.ID, 'recovery-phone-btn')
    EMAIL_BUTTON = (By.ID, 'recovery-email-btn')
    QRCODE_BUTTON = (By.ID, 'qr-section')
    SUPPORT_BUTTON = (By.ID, 'support-contact-btn')


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QRCODE_BUTTON)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
