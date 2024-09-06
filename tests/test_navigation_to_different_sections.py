from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.URLs import base_url
from src.locators import NavigationsTabsLocators
from src.conftest import driver


def test_section_navigation_sauces_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.BUTTON_SAUCE).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.HEADER_SAUCES)))

    section_header = driver.find_element(*NavigationsTabsLocators.HEADER_SAUCES)
    assert section_header.is_displayed()


def test_section_navigation_fillings_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.BUTTON_FILLING).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.HEADER_FILLINGS)))

    assert driver.find_element(*NavigationsTabsLocators.HEADER_FILLINGS).is_displayed()


def test_section_navigation_buns_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.BUTTON_FILLING).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.HEADER_FILLINGS)))

    driver.find_element(*NavigationsTabsLocators.BUTTON_BUNS).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.HEADER_BUNS)))

    assert driver.find_element(*NavigationsTabsLocators.HEADER_BUNS).is_displayed()
