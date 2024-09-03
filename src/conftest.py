import pytest
from selenium import webdriver
from src.helpers import generate_login, generate_password #импорт генераторов из helpers


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function") #фикстура для генератора логина
def login():
    return generate_login(length=8)

@pytest.fixture(scope="function") #фикстура для генератора пароля
def password():
    return generate_password(length=8)
