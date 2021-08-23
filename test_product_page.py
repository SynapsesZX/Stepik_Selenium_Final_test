import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.product_page import BookPage
from pages.busket_page import BusketPage
from pages.login_page import LoginPage

from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC


from pages.product_page import ProductPageLocators

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offerN'
    page = BookPage(browser,link)
    page.open_link()
    page.adding_to_the_cart()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.see_cart_button()
    busket_page = BusketPage(browser,browser.current_url)
    busket_page.should_be_the_same_price()



#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, link):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offerN'

@pytest.mark.skip
def test_guest_cant_see_success_message_before_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open_link()
    page.adding_to_the_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open_link()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BookPage(browser, link)
    page.open_link()
    page.adding_to_the_cart()
    page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage (browser, link)
    page.open_link()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage (browser, link)
    page.open_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open_link()
    page.see_cart_button()
    page = BusketPage(browser, browser.current_url)
    page.product_should_be_not_present()
    page.check_busket_empty_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function",autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page =LoginPage(browser,link)
        page.open_link()
        page.go_to_login_page()
        page.register_new_user()
        page.reg_button()
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BookPage(browser, link)
        page.open_link()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offerN'
        page = BookPage(browser, link)
        page.open_link()
        page.adding_to_the_cart()
        page.solve_quiz_and_get_code()
        page.check_product_name()
        page.see_cart_button()
        busket_page = BusketPage(browser, browser.current_url)
        busket_page.should_be_the_same_price()


