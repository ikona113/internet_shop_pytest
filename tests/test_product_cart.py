import time

from page.homepage import HomePage
from page.cart_page import CartPage
from conftest import driver



def test_cart(driver):
    """Проверяем, что при добавлении 1 товара в корзину, у корзины отображается иконка с цифрой 1"""
    homepage=HomePage(driver)
    cartpage=CartPage(driver)
    homepage.open()
    try:
        homepage.accept_agree()
    except Exception:
        print('Не появилось окно с куки')
    homepage.click_argus()
    cartpage.click_size_m()
    cartpage.click_color_gray()
    cartpage.click_add_to_cart()
    cartpage.display_cart_one_element()