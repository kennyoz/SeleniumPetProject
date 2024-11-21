

import pytest
from pages.login import Login_input
from pages import Constants



def test_valid_login_input(driver):
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()


def test_input_value_name_and_password(driver):
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_valid_name_and_login()

def test_input_valid_name_and_invalid_password(driver):
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_invalid_name_and_valid_password()


def test_input_invalid_name_and_valid_password(driver):
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_invalid_name_and_valid_password()
