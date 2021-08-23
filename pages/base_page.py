import time
from telnetlib import EC
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators, ProductPageLocators
import math
from selenium.webdriver.support.wait import WebDriverWait
import random
from random import randint


class BasePage():
    def __init__(self,browser,url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_link(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
#is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
             WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
#is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True



    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def see_cart_button(self):
        show_cart_button = self.browser.find_element(*ProductPageLocators.SHOW_CART_BUTTON)
        show_cart_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
# Random Generators #
    def randomWord(length=10):
        consonants = "abcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))

        # функция на рандомные имена кирилица

    def randomWord_rus(length=10):
        consonants = "абгдеёжзийклмнопрстуфхцчшщыьэюя"
        vowels = "абгдеёжзийклмнопрстуфхцчшщыьэюя"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))

        # функция на лучшие пароли

    def randomWord_passwords(length=10):
        consonants = "ABCDIFGKGIFOGJFLGOOOfgfgfgfgferytyijyyuyyyyy1234567890"
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))

        # функция на рандомные почты

    def randomWord_mails(length=10):
        consonants = "abcdfghjklmnpqrstvwxyz"
        email = '@gmail.com'
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length)) + email

        # функция на рандомные телефоны

    def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    for mciNumbers in range(0, 100):
        pass