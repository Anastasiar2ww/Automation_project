import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class Main_page(Base):

    global_1_text = ''  # текст 1ого продукта на главной
    global_1_price = '' # цена 1ого продукта на главной
    global_2_text = ''  # текст 2ого продукта на главной
    global_2_price = '' # цена 2ого продукта на главной

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    search_field = '//input[@id="smart-title-search-input"]' # поле поиска
    phones_menu = '//*[@id="js-drop-header"]/div[2]/ul/li[6]/a'     # меню Cмартфон
    text_phones = "//h1[@class = 'page-head__title']"   # текст Сматрфоны
    correct_text = "Смартфоны"  # корректный текст
    high_price_field = '//input[@name="arrFilter_P1_MAX"]'  # поле цены верхней
    sort_price = '//a[@data-sort="CATALOG_PRICE_1"]'    # кнопка сортировки цены
    checkbox_iphone = '//*[@id="page-side"]/form/fieldset[2]/div/div/label/span'    # чек бокс теги Iphone
    checkbox_memory = '//*[@id="page-side"]/form/fieldset[20]/div/div/label[2]/span'    # чек бокс
    phone_1_text = '/html/body/div[1]/main/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]' # текст 1ого телефона
    phone_1_price = '//*[@id="catalog"]/div[1]/div/div[3]/div[1]/div[2]' # цена 1ого телефона
    phone_1_button = '//a[@product-id="23224"]' # кнопка Купить 1ого телефона
    buy_button = '//div[@class="product-price__buy"]' # кнопка Купить
    return_to_shop = '//a[@onclick="bx_basketFKauiI.popup.close()"]' # кнопка вернуться в магазин
    phone_2_text = '/html/body/div[1]/main/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]' # текст 2ого телефона
    phone_2_price = '//*[@id="catalog"]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[2]' # цена 2ого телефона
    phone_2_button = '//a[@product-id="23225"]' # кнопка Купить 2ого телефона
    cart = "//*[text()='В корзину']" # кнопка В корзину

        # Getters

    def get_search_field(self): # поле поиска
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.search_field)))

    def get_phones_menu(self): # поле меню смартфона
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones_menu)))

    def get_text_phones(self):  # текс Смартфоны
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_phones)))

    def get_high_price_field(self): # поле цены верхней
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.high_price_field)))

    def get_sort_price(self):   # сортировка цены
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_price)))

    def get_checkbox(self): # чекбокс тег Iphone
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_iphone)))

    def get_checkbox_memory(self):  # чекбокс памяти 128gb
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_memory)))

    def get_phone_1(self):  # кнока 1 телефона
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1_button)))

    def get_phone_1_text(self): # текст 1ого телефона
        value_phone_1_text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1_text)))
        Main_page.global_1_text = value_phone_1_text.text
        print( f" Get 1st product text main:: {Main_page.global_1_text}")
        return Main_page.global_1_text

    def get_phone_1_price(self):    # цена 1ого телефона
        value_phone_1_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1_price)))
        Main_page.global_1_price = value_phone_1_price.text
        Main_page.global_1_price = Main_page.global_1_price.replace("a", "").replace(" ", "")
        print(f" Get 1st product price main:: {Main_page.global_1_price}")
        return Main_page.global_1_price

    def get_phone_1_button(self):   # кнопка Купить 1 телефон
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1_button)))

    def get_buy_button(self):   # кнопка купить после выбора телефона
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_return_to_shop(self):   # кнопка вернуться в магазин
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_to_shop)))

    def get_phone_2_text(self):     # получить текст 2ого телефона
        value_phone_2_text = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_2_text)))
        Main_page.global_2_text = value_phone_2_text.text
        print(f" Get 2nd product text main: {Main_page.global_2_text}")
        return Main_page.global_2_text

    def get_phone_2_price(self):    # получить цену 2ого телефона
         value_phone_2_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_2_price)))
         Main_page.global_2_price = value_phone_2_price.text
         Main_page.global_2_price = Main_page.global_2_price.replace("a", "").replace(" ", "")
         print(f" Get 2nd product price main: {Main_page.global_2_price}")
         return Main_page.global_2_price

    def get_phone_2_button(self):   # кнопка Купить 2ого телефона
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_2_button)))

    def get_cart(self): # кнопка в Корзину
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions
    """ Проверка видиомости поля поиска """
    def check_visible_search_field(self):
        self.get_search_field()
        print("Search field is visible")
        # self.get_search_field().send_keys("Iphone 15 Pro Max")
        # assert "Iphone 15 Pro Max" in self.driver.page_source
        # print("text in search_field is correct")
        # self.driver.refresh()

    """ Выбрали в меню по сматрфонам """
    def click_phones(self):
        self.get_phones_menu().click()
        print("Click phones")

    """ Ввели цену в поле """
    def get_in_high_price_field(self,price):
        self.get_high_price_field().clear()
        self.get_high_price_field().send_keys(price)
        self.get_high_price_field().send_keys(Keys.RETURN)
        self.driver.execute_script("window.scrollBy(0,200)", "")
        print("send get_high_price_field")

    """ Выбрали сортировку по цене """
    def click_sort_price(self):
        self.get_sort_price().click()
        print("click sort of price")

    """ Выбрали чек бокс "Теги Iphone" """
    def click_get_checkbox(self):
        self.get_checkbox().click()
        print("click checkbox Iphone")

    """ Выбрали ек бокс Память 128gb """
    def click_get_checkbox_memory(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_checkbox_memory())
        checkbox = self.get_checkbox_memory()
        checkbox.click()
        # time.sleep(1)
        # assert checkbox.is_selected()
        # print("чекбокс выбран")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 20)")
        time.sleep(1)
        print("click checkbox memory 128gb")

    """ Нажали на 1ый продукт """
    def click_phone_1(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_phone_1())
        self.get_phone_1().click()
        print("click buy 1st phone")

    """ Нажали на купить 1ый продукт """
    def click_buy_button(self):
        self.get_buy_button().click()
        print("click buy 1st product")
        time.sleep(2)

    """ Нажали на Войти в корзину """
    def click_return_to_shop(self):
        self.get_return_to_shop().click()
        self.driver.back() # перешли назад на страницу
        print("click enter to cart")

    """ Нажали на купить 2ой продукт """
    def click_phone_2_button(self):
        self.get_phone_2_button().click()
        print("click buy 2st phone")

    """ Перешли в корзину """
    def click_cart(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_cart())
        self.get_cart().click()
        print("click cart")

    # Methods
    """ Выбор продуктов """
    def select_phones(self):
        self.check_visible_search_field()
        self.get_current_url()
        self.click_phones()
        self.get_in_high_price_field(200000)
        self.click_sort_price()
        self.click_get_checkbox()
        self.click_get_checkbox_memory()
        self.get_phone_1_text()
        self.get_phone_1_price()
        self.click_phone_1()
        self.click_buy_button()
        self.click_return_to_shop()
        self.get_phone_2_text()
        self.get_phone_2_price()
        self.click_phone_2_button()
        self.click_cart()
        time.sleep(1)





