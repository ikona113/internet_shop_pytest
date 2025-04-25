from page.homepage import HomePage
from conftest import driver



def test_asd(driver):
    homepage=HomePage(driver)
    homepage.accept_agree()
    homepage.click_argus()