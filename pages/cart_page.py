from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):

    cart_url = 'https://pitergsm.ru/personal/cart/' # url стрницы корзины

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    get_order = '//button[@value="Оформить заказ"]' # кнопка Оформить заказ
    order_box = '//div[@class="cart-prod"]' # Локатор cart-item для товара


        # Getters

    """ Получили кнопку заказа """
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.get_order)))

    """ Получили кол-во товаров в корзине по cart-item """
    def get_order_box(self): #
        return self.driver.find_elements(By.XPATH, self.order_box)

        # Actions

    """ Нажали на кнопку заказа """
    def click_order_button(self):
        self.get_order_button().click()
        print("Click order_button")

        # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.assert_url(self.cart_url)
        self.count_of_product(self.get_order_box(),2)
        self.click_order_button()




