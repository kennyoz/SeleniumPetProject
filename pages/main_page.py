from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.conftest import driver





class Main_page(BasePage):
    #locators
    price_comporision = (By.XPATH,"//*[@class='svg svg-inline-compare big inline ']")     #СРАВНЕНИЕ
    price_comporicion_assert = (By.XPATH,"//*[@class='notetext']")                        #чек ПЕРЕХОДА
    basket_button_main_menu = (By.XPATH,"//*[@class='svg basket big inline ']")           #кнопка корзины
    enter_cart_assert = (By.XPATH,"//*[@id='pagetitle']")                                 #чек перехода в корзину
    catalog_button = (By.XPATH,"//*[@class='fuksia_but']")                                #кнопка каталога
    move_to_catalog_assert = (By.XPATH,"//*[@id='pagetitle']")                            #чек перехода в каталог
    search_input = (By.XPATH,"//*[@id='title-search-input1']")                            #инпут поиска на главной странице
    find_after_search = (By.XPATH,"//*[@class='digi-title']")                             #чек осуществления поиска
    button_auto_products = (By.XPATH,"//*[@id='bx_3950363924_25132']")                    #кнопка автопродукты
    auto_products_assert_to_move = (By.XPATH,"//*[@id='bx_1847241719_25625']")            #чек осуществления перехода в автопродукты


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


    def click_to_the_button_auto_products(self):
        self.click_element(Main_page.button_auto_products)
        self.is_element_visible(Main_page.auto_products_assert_to_move)


