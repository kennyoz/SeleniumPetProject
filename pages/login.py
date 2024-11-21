import pytest
from pages.main_page import Main_page
from pages.base_page import BasePage
from pages import Constants
from selenium.webdriver.common.by import By
from tests.conftest import driver
import time



class Login_input(BasePage):
    #локаторы
    button_login_input = (By.XPATH,"//*[@class='wrap_icon inner-table-block1 person']")         #кнопка логина на главной странице
    placeholder_login = (By.XPATH,"//*[@class='popup-singin']")                                 # локатор плейхолдера лк
    input_login_in_placeholder = (By.XPATH,"//*[@id='USER_LOGIN_POPUP']")                       # поле инпут логин
    input_password_in_placeholder = (By.XPATH,"//*[@id='USER_PASSWORD_POPUP']")                 # поле инпут пароль
    block_error = (By.XPATH,"//*[@class='filter block error']")                                 # чек ошибки при неверном заполнении
    login_button_in_placeholder = (By.XPATH,"//*[@data-type='phone']")                          # кнопка входа с заполненым логином и паролем


    def find_and_click_login(self):                                                                #клик на кнопку входа в личный кабинет
        self.is_element_visible(Login_input.button_login_input)
        self.find_element(Login_input.button_login_input).click()
        self.is_element_visible(Login_input.placeholder_login)


    def enter_valid_name_and_login(self):                                                                   #
        self.find_element(Login_input.input_login_in_placeholder).send_keys(Constants.LOGIN)
        self.find_element(Login_input.input_password_in_placeholder).send_keys(Constants.PASSWORD)
        self.find_element(Login_input.login_button_in_placeholder).click()
        self.is_element_visible(Login_input.block_error)


    def enter_invalid_name_and_valid_password(self):                                                        #
        self.find_element(Login_input.input_login_in_placeholder).send_keys(Constants.INVALID_LOGIN)
        self.find_element(Login_input.input_password_in_placeholder).send_keys(Constants.PASSWORD)
        self.find_element(Login_input.login_button_in_placeholder).click()
        self.is_element_visible(Login_input.block_error)



    def enter_name_and_invalid_password(self):
        self.find_element(Login_input.input_login_in_placeholder).send_keys(Constants.LOGIN)
        self.find_element(Login_input.input_password_in_placeholder).send_keys(Constants.INVALID_PASSWORD)
        self.find_element(Login_input.login_button_in_placeholder).click()
        self.is_element_visible(Login_input.block_error)


    def enter_invalid_name_invalid_password(self):
        self.find_element(Login_input.input_login_in_placeholder).send_keys(Constants.INVALID_LOGIN)
        self.find_element(Login_input.input_password_in_placeholder).send_keys(Constants.INVALID_PASSWORD)
        self.find_element(Login_input.login_button_in_placeholder).click()
        self.is_element_visible(Login_input.block_error)
