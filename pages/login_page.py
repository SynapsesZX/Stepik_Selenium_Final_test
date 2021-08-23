from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import LoginPageLocators,UserRegistration


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login URL is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self,email='',password=''):
        self.email = email
        self.password = password
        write_email = self.browser.find_element(*UserRegistration.SEND_EMAIL)
        write_email.click()
        write_email.send_keys(BasePage.randomWord_mails())
        write_password = self.browser.find_element(*UserRegistration.SEND_PASSWORD)
        write_password.click()
        write_password.send_keys("Igjhgjhgkk59970505965955")
        write_second_password = self.browser.find_element(*UserRegistration.SEND_PASSWORD_AGAIn)
        write_second_password.click()
        write_second_password.send_keys("Igjhgjhgkk59970505965955")

    def reg_button(self):
        reg_button = self.browser.find_element(By.CSS_SELECTOR,'[name="registration_submit"]')
        reg_button.click()

