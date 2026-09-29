import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


