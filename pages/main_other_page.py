from lib2to3.pgen2 import driver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from pages.main_page import Main_page


class Main_other_page(Base):

    url = 'https://stackoverflow.com/'


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    text_product = '//a[@aria-controls="products-popover"]'


    # Getters

    def get_text_product(self): # спарсили слово продукт с гланой страницы
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.text_product)))

   # Actions

    def check_text_product(self):
        value_text = self.get_text_product()
        value_text = value_text.text # получили слово - Продукт

        a = Main_page(driver) # получили эзкемаляр класса Main_page()

        text_2_main = a.global_2_text # достпали глобальную переменную текста второго продукта с главной странницы

        print(f"Текст на новой странице:  {value_text}")
        print(f"Текст на старой странице:  {text_2_main}")

        #self.driver.get('https://stackoverflow.com/questions')



    def input_link(self):
        self.driver.get(self.url)
        self.check_text_product()
