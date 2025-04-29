import time

from conftest import driver
from page.account_page import AccountPage
from page.homepage import HomePage

def test_select_xs_element(driver):
    """Тест на кнопку xs размера"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_size_xs()
    homepage.display_xs_selected()

def test_select_blue_color(driver):
    """Тест на кнопку blue цвета"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_color_Blue()
    homepage.display_blue_color_selected()

def test_promo_picture_proceed_to_collection(driver):
    """Тест на промо картинку ведущую в нужную(expected_url) коллекцию"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_promo_picture()
    expected_url = 'https://magento.softwaretestingboard.com/collections/yoga-new.html'
    homepage.display_new_url_for_expected_url(expected_url)

def test_sign_in_open_url_login(driver):
    """Тест на проверку открытия url с авторизацией по кнопке sign in"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_sign_in()
    expected_url = 'https://magento.softwaretestingboard.com/customer/account/login/'
    homepage.display_new_url_for_expected_url(expected_url)

def test_create_an_account_open_url_create(driver):
    """Тест на проверку открытия url с регистрацией по кнопке create an account"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_create_an_account()
    expected_url = 'https://magento.softwaretestingboard.com/customer/account/create/'
    homepage.display_new_url_for_expected_url(expected_url)

def test_registration_from_homepage(driver):
    """Тест на прохождение регистрации с главной страницы"""
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_create_an_account()
    accountpage = AccountPage(driver)


    first_name = 'Artem1'
    last_name = 'Ikonnikov1'
    email = 'asssdd1@mail.ru'
    password = 'Aassdd113.'
    confirm_password = 'Aassdd113.'
    accountpage.input_first_name(first_name)
    accountpage.input_last_name(last_name)
    accountpage.input_email(email)
    accountpage.input_password(password)
    accountpage.input_confirm_password(confirm_password)
    accountpage.click_create_an_account()
    accountpage.display_new_url_for_registration()