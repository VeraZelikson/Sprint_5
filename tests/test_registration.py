from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.helpers import generate_login, generate_password
from src.conftest import driver
from src.URLs import register_url
from src.locators import RegisterFormLocators, LoginFormLocators

def test_registration_form_successful(driver):
    driver.get(register_url)
    password = generate_password(length=8)
    login = generate_login(length=8)

    driver.find_element(*RegisterFormLocators.input_name).send_keys("Vera_Z_Name_13")
    driver.find_element(*RegisterFormLocators.input_login).send_keys(login)
    driver.find_element(*RegisterFormLocators.input_password).send_keys(password)
    driver.find_element(*RegisterFormLocators.button_register).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LoginFormLocators.label_enter)))

    assert driver.find_element(*LoginFormLocators.label_enter).is_displayed()

def test_registration_form_failed(driver):
    driver.get(register_url)
    login = generate_login(length=8)

    driver.find_element(*RegisterFormLocators.input_name).send_keys("Vera_Z_Name_13")
    driver.find_element(*RegisterFormLocators.input_login).send_keys(login)
    driver.find_element(*RegisterFormLocators.input_password).send_keys('123')
    driver.find_element(*RegisterFormLocators.button_register).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((RegisterFormLocators.label_error)))

    assert driver.find_element(*RegisterFormLocators.label_error).is_displayed()