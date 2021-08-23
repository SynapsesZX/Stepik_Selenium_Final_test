from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.locators import BusketPageLocators,BusketCheck


class BusketPage(BasePage):

    def should_be_the_same_price(self):
        check_product_price = self.browser.find_element(*BusketPageLocators.CHECK_CART_PRODUCT_PRICE)
        check_product_price_general = self.browser.find_element(*BusketPageLocators.CHECK_CART_GENERAL_PRICE)
        assert check_product_price.text == check_product_price_general.text, 'The price is not the same'
        print('Всё отлично цена совпадает')

    def product_should_be_not_present(self):
        assert self.is_not_element_present(*BusketCheck.CHECK_BUSKET_ITEMS)
        print('Good, There are no items in the Busket')

    def check_busket_empty_message(self):
        assert self.is_element_present(*BusketCheck.CHECK_BUSKET_EMPTY_PRODUCTS_TEXT)
        print('Good,There is text with your busket is empty')