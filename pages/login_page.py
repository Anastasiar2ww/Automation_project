from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Login_page(Base):
    url = 'https://pitergsm.ru/'
    # url_correct = "https://telemarket24.ru/?login=yes" # url после авторизации

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    input_button = '//div[@class="sh-nav__col"]'    # кнопка входа в ЛК
    user_name = '//input[@name="USER_LOGIN"]'   # поле user_name
    password = '//input[@name="USER_PASSWORD"]'     # поле password
    login_button = '//input[@value="Войти"]'    # поле Войти
    my_account = "//*[text()='Личный кабинет']"     # Личный кабинет


        # Getters

    def get_input_button(self): # кнопка Войти
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_button)))

    def get_user_name(self):    # Поле user_name
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):     # Поле password
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self): # кнопка Войти
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_my_account(self): # Мой аккаунт
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.my_account))).text

    # Actions

    """ Нажали на войти """
    def click_input_button(self):
        self.get_input_button().click()
        print("Click input_button_1")

    """ Ввели user_name """
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    """ Ввели password """
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    """ Нажали на Войти """
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    """ Проверили, что есть Мой аккаунт """
    def assert_correct_url(self):
        self.get_my_account()
        print("Element my account is exist")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_input_button()
        self.input_user_name('')
        self.input_password('')
        self.click_login_button()
        self.assert_correct_url()



