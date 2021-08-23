import time

from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import BookPage
from pages.busket_page import BusketPage
import pytest









def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open_link()
    page.go_to_the_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_link()
    page.should_be_login_link()


def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_register_form()

def test_guest_can_go_to_login_page_with_return(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open_link()
    page.go_to_the_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_busket_items(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = BookPage(browser,link)
    page.open_link()
    page.see_cart_button()
    page = BusketPage(browser,browser.current_url)
    page.product_should_be_not_present()
    page.check_busket_empty_message()



