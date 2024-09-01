from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import test_data
from src.URLs import base_url
from src.locators import LoginFormLocators, RegisterFormLocators, MainPageLocators, OrderButtonIsDisplayedLocators,PersonalAccountLocators
from src.conftest import driver
def test_move_to_personal_account(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()

    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    section_header = driver.find_element(*OrderButtonIsDisplayedLocators.button_order)
    assert section_header.is_displayed()

def test_move_from_personal_account_to_constructor_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()

    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()
    driver.find_element(*MainPageLocators.button_constructor).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.header_make_burger)))

    assert driver.find_element(*MainPageLocators.header_make_burger).is_displayed()

def test_move_from_personal_account_to_logo_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()

    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()
    driver.find_element(*MainPageLocators.button_burger_logo).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.header_make_burger)))

    section_header = driver.find_element(*MainPageLocators.header_make_burger)
    assert section_header.is_displayed()

def test_move_from_personal_account_to_logout_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()

    driver.find_element(*LoginFormLocators.input_email_login).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.input_password).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.button_login).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.button_order)))

    driver.find_element(*PersonalAccountLocators.personal_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((PersonalAccountLocators.link_profile)))
    driver.find_element(*PersonalAccountLocators.button_logout).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LoginFormLocators.label_enter)))

    section_header = driver.find_element(*LoginFormLocators.label_enter)
    assert section_header.is_displayed()
