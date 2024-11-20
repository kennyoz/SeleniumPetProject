import pytest

from pages.main_page import  Main_page
import time
from tests.conftest import driver


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








