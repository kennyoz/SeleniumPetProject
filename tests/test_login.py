

import pytest
from pages.login import Login_input
from pages import Constants


@pytest.mark.smoke
def test_valid_login_input(driver):                                             #клик на кнопку личный кабинети проверка видимости плейсхолдера
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()

@pytest.mark.smoke
def test_input_value_name_and_password(driver):                                 #Ввод валидного логина и пароля
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_valid_name_and_login()

@pytest.mark.smoke
def test_input_valid_name_and_invalid_password(driver):                          #Ввод валидного логина и невалидного пароля
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_invalid_name_and_valid_password()

@pytest.mark.smoke
def test_input_invalid_name_and_valid_password(driver):                             #Ввод невалидного логина и валидного пароля
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_name_and_invalid_password()

@pytest.mark.smoke
def test_input_invalid_name_and_invalid_password(driver):                           #ввод невалидного имени и невалидного пароля
    driver.get(Constants.URL)
    login = Login_input(driver)
    login.find_and_click_login()
    login.enter_invalid_name_invalid_password()

