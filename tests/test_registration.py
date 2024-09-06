from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.conftest import driver, password, login
from src.URLs import register_url
from src.locators import RegisterFormLocators, LoginFormLocators

def test_registration_form_successful(driver, login, password):
    driver.get(register_url)

    driver.find_element(*RegisterFormLocators.INPUT_NAME).send_keys("Vera_Z_Name_13")
    driver.find_element(*RegisterFormLocators.INPUT_LOGIN).send_keys(login)
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*RegisterFormLocators.BUTTON_REGISTER).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LoginFormLocators.LABEL_ENTER)))

    assert driver.find_element(*LoginFormLocators.LABEL_ENTER).is_displayed()

def test_registration_form_failed(driver, login):
    driver.get(register_url)

    driver.find_element(*RegisterFormLocators.INPUT_NAME).send_keys("Vera_Z_Name_13")
    driver.find_element(*RegisterFormLocators.INPUT_LOGIN).send_keys(login)
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys('123')
    driver.find_element(*RegisterFormLocators.BUTTON_REGISTER).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((RegisterFormLocators.LABEL_ERROR)))

    assert driver.find_element(*RegisterFormLocators.LABEL_ERROR).is_displayed()