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

    # локатары для - https://ok.ru/
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id = "enter-action"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@data-test-id="forgot-password-link"]' )
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-test-id="registration-action"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    REGISTRATION_QR_BUTTON = (By.XPATH, '//*[@label="Войти по QR-коду"]')


class LoginPageHelper(BasePage):
    pass