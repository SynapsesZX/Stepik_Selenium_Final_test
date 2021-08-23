from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR,'#login_link')
    LOGIN_FORM = (By.CLASS_NAME,'login_form')
    REGISTER_FORM = (By.ID,'register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR,"button[value='Добавить в корзину']")
    SHOW_CART_BUTTON = (By.CSS_SELECTOR,"a[class='btn btn-default']")
    CHECK_PRODUCT_NAME_RESULT = (By.CSS_SELECTOR,".alertinner strong")
    CHECK_PRODUCT_NAME_GENERAL = (By.CSS_SELECTOR,"li[class='active']")
    ALERT = (By.CSS_SELECTOR,"div .alert-success")

class BusketPageLocators():
     CHECK_CART_PRODUCT_PRICE = (By.CSS_SELECTOR,"div[class='col-sm-1'] p[class='price_color align-right']")
     CHECK_CART_GENERAL_PRICE = (By.CSS_SELECTOR,"div[class='col-sm-2'] p[class='price_color align-right']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BusketCheck():
    CHECK_BUSKET_ITEMS = (By.CLASS_NAME,".basket-items")
    CHECK_BUSKET_EMPTY_PRODUCTS_TEXT = (By.XPATH,"//*[contains(text(), 'Your basket is empty.')]")

class UserRegistration():
    SEND_EMAIL = (By.CSS_SELECTOR,'[name="registration-email"]')
    SEND_PASSWORD = (By.CSS_SELECTOR,'[name="registration-password1"]')
    SEND_PASSWORD_AGAIn = (By.CSS_SELECTOR,'[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR,'[name="registration_submit"]')