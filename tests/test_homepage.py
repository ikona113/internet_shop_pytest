from conftest import driver
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

