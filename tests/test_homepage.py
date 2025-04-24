from conftest import driver
from page.homepage import HomePage

def test_cart(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_argus()
