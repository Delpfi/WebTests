from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = "https://sn.rv-school.ru/"
EMPTY_LOGIN_ERROR = "Введите телефон, email или логин и пароль."
LOGIN_TEXT = "logiinnnnnnnn123"

def test_empty_login_and_password(browser): #browser - фикструка, которую нужно вызвать
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


def test_send_keys_text(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage2 = LoginPageHelper(browser)
    LoginPage2.send_keys_text(LOGIN_TEXT)
    LoginPage2.click_login()
    assert LoginPage2.get_error_text() == EMPTY_LOGIN_ERROR




