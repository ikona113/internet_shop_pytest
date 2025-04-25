import time

from page.homepage import HomePage
from page.cart_page import CartPage
from conftest import driver



def test_cart(driver):
    homepage=HomePage(driver)
    cartpage=CartPage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_argus()
    cartpage.click_size_m()
    cartpage.click_color_gray()
    cartpage.click_add_to_cart()
    cartpage.display_cart_one_element()