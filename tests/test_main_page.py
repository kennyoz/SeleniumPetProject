import pytest

from pages.main_page import  Main_page
import time
from tests.conftest import driver
URL = "https://www.virage24.ru/"
input_search = "труба профильная"

@pytest.mark.smoke
def test_price_comparison_click(driver):
    driver.get("https://www.virage24.ru/")
    main_page = Main_page(driver)
    main_page.click_to_price_comporition()

@pytest.mark.smoke
def test_cart_button(driver):
    driver.get("https://www.virage24.ru/")
    main_page = Main_page(driver)
    main_page.click_to_cart_and_cheack()


@pytest.mark.smoke
def test_move_to_catalog(driver):
    driver.get(URL)
    main_page = Main_page(driver)
    main_page.click_to_the_catalog()

@pytest.mark.smoke
def test_to_search(driver):
    driver.get(URL)
    main_page= Main_page(driver)
    main_page.input_to_the_search()

@pytest.mark.regress
def test_click_to_the_auto_products(driver):
    driver.get(URL)
    main_page = Main_page(driver)
    main_page.click_to_the_button_auto_products()















