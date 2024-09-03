from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.data import test_data
from src.URLs import base_url
from src.locators import LoginFormLocators, RegisterFormLocators, MainPageLocators, OrderButtonIsDisplayedLocators,PersonalAccountLocators
from src.conftest import driver
def test_move_to_personal_account(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    section_header = driver.find_element(*OrderButtonIsDisplayedLocators.BUTTON_ORDER)
    assert section_header.is_displayed()

def test_move_from_personal_account_to_constructor_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.BUTTON_CONSTRUCTOR).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.HEADER_MAKE_BURGER)))

    assert driver.find_element(*MainPageLocators.HEADER_MAKE_BURGER).is_displayed()

def test_move_from_personal_account_to_logo_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*MainPageLocators.BUTTON_BURGER_LOGO).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.HEADER_MAKE_BURGER)))

    section_header = driver.find_element(*MainPageLocators.HEADER_MAKE_BURGER)
    assert section_header.is_displayed()

def test_move_from_personal_account_to_logout_true(driver):
    driver.get(base_url)

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginFormLocators.INPUT_EMAIL_LOGIN).send_keys(test_data['login'])
    driver.find_element(*RegisterFormLocators.INPUT_PASSWORD).send_keys(test_data['password'])
    driver.find_element(*LoginFormLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((OrderButtonIsDisplayedLocators.BUTTON_ORDER)))

    driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((PersonalAccountLocators.LINK_PROFILE)))
    driver.find_element(*PersonalAccountLocators.BUTTON_LOGOUT).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LoginFormLocators.LABEL_ENTER)))

    section_header = driver.find_element(*LoginFormLocators.LABEL_ENTER)
    assert section_header.is_displayed()
