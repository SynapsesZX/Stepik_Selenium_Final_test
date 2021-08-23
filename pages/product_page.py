from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators


class BookPage(BasePage):


    def adding_to_the_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT),"Success message is presented, but should not be"

    def should_be_product_name_result(self):
        assert self.is_element_present(*ProductPageLocators.CHECK_PRODUCT_NAME_RESULT), "The product name result is not presented"

    def should_be_product_name_general(self):
        assert self.is_element_present(*ProductPageLocators.CHECK_PRODUCT_NAME_GENERAL), "The general product name is not presented"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT),'The element isnt disappeared'

    def check_product_name(self):
        check_product_name_result = self.browser.find_element(*ProductPageLocators.CHECK_PRODUCT_NAME_RESULT)
        check_product_name_base = self.browser.find_element(*ProductPageLocators.CHECK_PRODUCT_NAME_GENERAL)
        assert check_product_name_result.text == check_product_name_base.text,'The text is not the same'
        print('Всё отлично названия совпадают')



    def check_alert_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT), "Success message is presented, but should not be"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"



