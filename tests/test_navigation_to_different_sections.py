from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.URLs import base_url
from src.locators import NavigationsTabsLocators
from src.conftest import driver


def test_section_navigation_sauces_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.button_sauce).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.header_sauces)))

    section_header = driver.find_element(*NavigationsTabsLocators.header_sauces)
    assert section_header.is_displayed()


def test_section_navigation_fillings_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.button_filling).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.header_fillings)))

    assert driver.find_element(*NavigationsTabsLocators.header_fillings).is_displayed()


def test_section_navigation_buns_true(driver):
    driver.get(base_url)

    driver.find_element(*NavigationsTabsLocators.button_filling).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.header_fillings)))

    driver.find_element(*NavigationsTabsLocators.button_buns).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NavigationsTabsLocators.header_buns)))

    assert driver.find_element(*NavigationsTabsLocators.header_buns).is_displayed()
