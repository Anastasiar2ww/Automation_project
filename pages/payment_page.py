import time
from lib2to3.pgen2 import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.main_page import Main_page


class Payment_page(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    email_filed = '//input[@autocomplete="email"]' # поле майл
    text_1_product_finish = '//*[@id="bx-soa-basket"]/li[1]/div[2]/a/h4'    # финишный текст 1ого продукта
    price_1_product_finish = '//*[@id="bx-soa-basket"]/li[1]/div[3]/div[1]/span'    # финишная цена 1ого продукта
    text_2_product_finish = '//*[@id="bx-soa-basket"]/li[2]/div[2]/a/h4'    # финишный текст 2ого продукта
    price_2_product_finish = '//*[@id="bx-soa-basket"]/li[2]/div[3]/div[1]/span'    # финишная цена 2ого продукта
    finish_price = '//*[@id="bx-soa-total-panel"]/div[2]/div[1]/span[2]' # финальная цена
    # Getters

    def get_email_filed(self):  # получили майл
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_filed)))

    def get_text_1_product_finish(self):    # текст 1ого продукта на финише
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_1_product_finish)))

    def get_text_2_product_finish(self):    # текст 2ого продукта на финише
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_2_product_finish)))

    def get_price_1_product_finish(self):   # цена 1ого продукта на финише
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_1_product_finish)))

    def get_price_2_product_finish(self):   # цена 2ого продукта на финише
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_2_product_finish)))

    def get_finish_prices(self):    # финишная сумма двух продуктов
        get_finish_prices_value = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_price)))
        get_finish_prices_value = get_finish_prices_value.text
        get_finish_prices_value = get_finish_prices_value.replace(" руб.", "").replace(" ", "")
        return get_finish_prices_value

    # Actions

    """ Удалили поле майл """ # оно обязательное, чтобы случайно не нажать на оформить при ручной проверке потом
    def clear_email(self):
        self.get_email_filed().clear()
        print("delete mail")

    """ Получили текст 1ого продукта с главной страницы """
    def get_text_1_from_main(self):
        a = Main_page(driver)
        text_1_main = a.global_1_text
        return text_1_main

    """ Получили текст 2ого продукта с главной страницы """
    def get_text_2_from_main(self):
        a = Main_page(driver)
        text_2_main = a.global_2_text
        return text_2_main

    """ Получили текст 1ого продукта с финишной страницы """
    def get_text_1(self):
        value_text_1 = self.get_text_1_product_finish().text
        return value_text_1

    """ Получили текст 2ого продукта с финишной страницы """
    def get_text_2(self):
        value_text_2 = self.get_text_2_product_finish().text
        return value_text_2

    """ Сравнили тексты 1ого продукта """
    def assert_text_of_1_products(self):
        assert self.get_text_1_from_main() == self.get_text_1()
        print("Text of 1 products is correct")

    """ Сравнили тексты 2ого продукта """
    def assert_text_of_2_products(self):
        assert self.get_text_2_from_main() == self.get_text_2()
        print("Text of 2 products is correct")

    """ Получили цену 1ого продукта с финишной страницы """
    def get_price_1(self):
        value_price_1 = self.get_price_1_product_finish().text
        value_price_1 = value_price_1.replace(" руб.", "").replace(" ", "")
        return value_price_1

    """ Получили цену 1ого продукта с главной страницы """
    def get_price_1_from_main(self):
        a = Main_page(driver)
        price_1_main = a.global_1_price
        return price_1_main

    """ Сравнили цены 1ого продукта """
    def assert_price_of_1_products(self):
        assert self.get_price_1_from_main() == self.get_price_1()
        print("Price of 1st products is correct")

    """ Получили цену 2ого продукта с финишной страницы """
    def get_price_2(self):
        value_price_2 = self.get_price_2_product_finish().text
        value_price_2 = value_price_2.replace(" руб.", "").replace(" ", "")
        return value_price_2

    """ Получили цену 2ого продукта с главной страницы """
    def get_price_2_from_main(self): # получили цену 2ого продукта с главной страницы
        a = Main_page(driver)
        price_2_main = a.global_2_price
        return price_2_main

    """ Сравнили цены 2ого продукта """
    def assert_price_of_2_products(self):
        assert self.get_price_2_from_main() == self.get_price_2()
        print("Price of 2nd products is correct")

    """ Сравнение финальной суммы  """
    def assert_sum_prices(self):
        value_price_1 = float(self.get_price_1())
        value_price_2 = float(self.get_price_2())
        total_price = value_price_1 + value_price_2
        finish_price = float(self.get_finish_prices())

        assert total_price == finish_price
        print(" Finish price is correct")

    # Methods
    def payment(self):
        self.get_current_url()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 20)")
        self.clear_email()
        self.assert_text_of_1_products()
        self.assert_text_of_2_products()
        self.assert_price_of_1_products()
        self.assert_price_of_2_products()
        self.assert_sum_prices()
        self.get_screenshot()
        #self.driver.get('https://pitergsm.ru/service/')











