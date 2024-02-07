import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Smart_watch_page(Base):


    correct_url_watch = 'https://telemarket24.ru/catalog/umnye_chasy_i_braslety/'


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    search_field_name = '//input[@name="arrFilter_FIELD_NAME"]'


        # Getters

    def get_search_field_name(self): # нижнее значение цены в поле
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field_name))).text


    # def get_field_price_high(self): # верхнее значение цены в поле
    #     fph = int(WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_price_high))).text)
    #     return fph

    # Actions

    def input_search_field_name(self, product_name):
        self.get_search_field_name().send_keys(product_name)
        print("Input low price")

    # def click_smart_watch(self):
    #     self.get_smart_watch().click()
    #     print("Click smart watch")

    """ Method assert price """

    # def drop_price_correct(self):
    #     #print(type(self.get_drop_price_low()))
    #
    #     value_price_low = 2000 # свдиг ползунка
    #
    #     low_value_drop_after = value_price_low + self.get_drop_price_low() # нижнее значение цены после сдвига ползунка
    #
    #     print( f"Нижнее значение цены в фильтре после сдвига ползунка на {value_price_low} должно быть = {low_value_drop_after}")
    #
    #     action = ActionChains(self.driver)
    #     action.click_and_hold(self.get_price()).move_by_offset(2000,0).release().perform() # сдвигаем ползунок цены на 20
    #     # print(self.get_drop_price_low())
        #
        # print(self.get_drop_price_low())


        # time.sleep(2)
        #
        # self.get_drop_price_high()
        #
        # print(self.get_field_price_low())
        #

        # print(type(self.get_field_price_low()))



        # vap = self.get_field_price_low()
        #
        # print(f"Нижняя цена в поле после сдвига  = {vap} ")
        # assert low_value_drop_after == vap




        # action.click_and_hold(self.get_price()).move_by_offset(value_price_low,0).release().perform()
        #
        # value_after_drop_low = int(self.get_drop_price_low()) + value_price_low
        # print(value_after_drop_low)

        #assert str(int(self.get_drop_price_low() + int(value_price_low))) == self.get_drop_price_low()





    # def click_select_product_2(self):
    #     self.get_select_product_2().click()
    #     print("Click select product_2")
    #
    # def click_select_product_3(self):
    #     self.get_select_product_3().click()
    #     print("Click select product_3")
    #
    # def click_cart(self):
    #     self.get_cart().click()
    #     print("Click cart")
    #
    # def click_menu(self):
    #     self.get_menu().click()
    #     print("Click menu")
    #
    # def click_link_about(self):
    #     self.get_link_about().click()
    #     print("Click link_about")

    # Methods

    def select_smart_watch(self):
        self.get_current_url()
        self.input_search_field_name("apple watch")
        self.assert_url(self.correct_url_watch)

    # def select_product_2(self):
    #     self.get_current_url()
    #     self.click_select_product_2()
    #     self.click_cart()
    #
    # def select_product_3(self):
    #     self.get_current_url()
    #     self.click_select_product_3()
    #     self.click_cart()
    #
    # def select_menu_about(self):
    #     self.get_current_url()
    #     self.click_menu()
    #     self.click_link_about()
    #     self.assert_url('https://saucelabs.com/')



