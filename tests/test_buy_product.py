from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

def test_buy_product_1(set_up, set_group):
    # настройка драйвера
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(r'C:\Users\Пользователь\PycharmProjects\resource\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_phones()

    cp = Cart_page(driver)
    cp.product_confirmation()

    p = Payment_page(driver)
    p.payment()



