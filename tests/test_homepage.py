from conftest import driver
from page.homepage import HomePage

def test_cart(driver):
    homepage = HomePage(driver)
    homepage.open_luma()
    homepage.accept_agree()
    homepage.click_argus()
    homepage.click_size_radiant_tee()
    homepage.click_gray_color_argus()
    homepage.click_add_to_cart_radiant_tee()
    homepage.display_cart_one_element()