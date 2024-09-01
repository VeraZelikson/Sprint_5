from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.locators import RegisterFormLocators, PersonalAccountLocators, LoginFormLocators, LoginButtonsLocators, OrderButtonIsDisplayedLocators
from src.conftest import driver
from src.URLs import base_url, restore_url, register_url
from src.data import test_data



def test_login_by_login_account_button(driver):

     driver.get(base_url)
     driver.find_element(*LoginButtonsLocators.button_login_main).click()
     driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
     driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
     driver.find_element(*LoginFormLocators.button_login).click()

     WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

     assert driver.find_element(*OrderButtonIsDisplayedLocators.button_order).is_displayed()


def test_login_by_personal_account_button(driver):
    driver.get(base_url)
    driver.find_element(*PersonalAccountLocators.personal_account_button).click()
    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    assert driver.find_element(*OrderButtonIsDisplayedLocators.button_order).is_displayed()

def test_login_registration_form(driver):
     driver.get(register_url)
     driver.find_element(*LoginButtonsLocators.label_enter_register).click()
     driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
     driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
     driver.find_element(*LoginFormLocators.button_login).click()

     WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

     assert driver.find_element(*OrderButtonIsDisplayedLocators.button_order).is_displayed()

def test_login_form_restore_password(driver):
    driver.get(restore_url)
    driver.find_element(*LoginButtonsLocators.button_login_restore).click()
    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    assert driver.find_element(*OrderButtonIsDisplayedLocators.button_order).is_displayed()


