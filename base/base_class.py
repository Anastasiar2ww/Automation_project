from datetime import datetime

class Base():
    # url = 'https://pitergsm.ru/'

    def __init__(self,driver):
        self.driver = driver


    """ Method get current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"current url: {get_url}")

    """ Method assert word """

    def assert_word(self,word,result): # word - слово на сайте, result - ожидаемое слово на сайте
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """ Method Screenshot """

    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'get_screenshot ' + now_date + '.png'

        self.driver.save_screenshot(r'C:\\Users\\Пользователь\PycharmProjects\Automation_in_Selenium\\screen\\' + name_screen)

    """ Method assert url """
    def assert_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """ Method assert count of product """
    def count_of_product(self,cart_item,count):
        assert len(cart_item) == count
        print("good test on count of product")



