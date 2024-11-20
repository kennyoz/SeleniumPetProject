from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.conftest import driver





class Main_page(BasePage):
    #locators
    price_comporision = (By.XPATH,"//*[@class='svg svg-inline-compare big inline ']")
    price_comporicion_assert = (By.XPATH,"//*[@class='notetext']")
    basket_button_main_menu = (By.XPATH,"//*[@class='svg basket big inline ']")
    enter_cart_assert = (By.XPATH,"//*[@id='pagetitle']")


    def click_to_price_comporition(self):                                           #проверка кнопки сравнение
        self.click_element(Main_page.price_comporision)
        self.is_element_visible(Main_page.price_comporicion_assert)


    def click_to_cart_and_cheack(self):                                             #проверка кнопки корзина
        self.click_element(Main_page.basket_button_main_menu)
        self.is_element_visible(Main_page.enter_cart_assert)

