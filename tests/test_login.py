from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import RegisterFormLocators, PersonalAccountLocators, LoginFormLocators, LoginButtonsLocators, OrderButtonIsDisplayedLocators
from src.conftest import driver
from src.URLs import base_url, restore_url, register_url
from src.data import test_data



def test_login_by_login_account_button(driver):

     driver.get(base_url)
     driver.find_element(*LoginButtonsLocators.BUTTON_LOGIN_MAIN).click()
     driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
     driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
     driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

     WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

     assert driver.find_element(*OrderButtonIsDisplayedLocators.BUTTON_ORDER).is_displayed()


def test_login_by_personal_account_button(driver):
    driver.get(base_url)
    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    assert driver.find_element(*OrderButtonIsDisplayedLocators.BUTTON_ORDER).is_displayed()

def test_login_registration_form(driver):
     driver.get(register_url)
     driver.find_element(*LoginButtonsLocators.LABEL_ENTER_REGISTER).click()
     driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
     driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
     driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

     WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

     assert driver.find_element(*OrderButtonIsDisplayedLocators.BUTTON_ORDER).is_displayed()

def test_login_form_restore_password(driver):
    driver.get(restore_url)
    driver.find_element(*LoginButtonsLocators.BUTTON_LOGIN_RESTORE).click()
    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    assert driver.find_element(*OrderButtonIsDisplayedLocators.BUTTON_ORDER).is_displayed()


