from conftest import driver
from page.homepage import HomePage

def test_select_xs_element(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.accept_agree()
    homepage.click_size_xs()
    homepage.display_xs_selected()
