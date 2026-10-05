import allure
import re

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = "https://sn.rv-school.ru/"

@allure.suite('Зарегистрироваться по телефону')
@allure.step('Проверка выбора из выпадающего списка код страны и номер')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Result_country_code = re.findall(r'\((.*?)\)',Selected_country_code)[0] #имитация получения данных с помощью регулярного выражения кода страны в поле телефон если оно было.
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Actual_country_code == Result_country_code



