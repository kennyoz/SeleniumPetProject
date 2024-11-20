from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.conftest import driver





class Main_page(BasePage):
    #locators
    price_comporision = (By.XPATH,"//*[@class='svg svg-inline-compare big inline ']")
    price_comporicion_assert = (By.XPATH,"//*[@class='notetext']")
    basket_button_main_menu = (By.XPATH,"//*[@class='svg basket big inline ']")
    enter_cart_assert = (By.XPATH,"//*[@id='pagetitle']")
    catalog_button = (By.XPATH,"//*[@class='fuksia_but']")
    move_to_catalog_assert = (By.XPATH,"//*[@id='pagetitle']")
    search_input = (By.XPATH,"//*[@id='title-search-input1']")
    find_after_search = (By.XPATH,"//*[@class='digi-title']")

    #value
    search_input_text= "труба профильная"






    def click_to_price_comporition(self):                                           #проверка кнопки сравнение
        self.click_element(Main_page.price_comporision)
        self.is_element_visible(Main_page.price_comporicion_assert)


    def click_to_cart_and_cheack(self):                                             #проверка кнопки корзина
        self.click_element(Main_page.basket_button_main_menu)
        self.is_element_visible(Main_page.enter_cart_assert)

    def click_to_the_catalog(self):                                                  #Проверка кнопки каталог
        self.click_element(Main_page.catalog_button)
        self.is_element_visible(Main_page.move_to_catalog_assert)

    def input_to_the_search(self):
        self.enter_text(Main_page.search_input,Main_page.search_input_text)
        self.submit_the_value(Main_page.search_input)
        self.is_element_visible(Main_page.find_after_search)


