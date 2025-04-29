import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открываем home page страницу"""
        self.driver.get('https://magento.softwaretestingboard.com/')

    def accept_agree(self):
        """Принимает предложение с куки"""
        button = self.driver.find_element(By.CSS_SELECTOR, "button[class=' css-1n36tvh']")
        button.click()

    def click_argus(self):
        """Переходим в карточку Argus All-Weather Tank"""
        element = self.driver.find_element(By.CSS_SELECTOR, 'span img[src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/m/t/mt07-gray_main_1.jpg"]')
        element.click()

    def click_radiant_tee(self):
        """Переходим в карточку Radiant Tee"""
        element = self.driver.find_element(By.CSS_SELECTOR, 'span img[src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/s/ws12-orange_main_2.jpg"]')
        element.click()

    def click_size_xs(self):
        """Кликаем по кнопке xs на первой карточке товара home page"""
        element = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Size"] > div[option-tooltip-value="XS"]')
        element.click()

    def display_xs_selected(self):
        """Проверяем что кнопка xs выбрана/подсвечена на 1 карточке товара home page"""
        cart = self.driver.find_element(By.CSS_SELECTOR, 'div[class="swatch-opt-1556"] > div[class="swatch-attribute size"]')
        wait = WebDriverWait(self.driver,5)
        value = cart.get_attribute('option-selected')

        assert int(value) == 166

    def click_color_Blue(self):
        """Кликаем по кнопке Blue на первой карточке товара home page"""
        button = self.driver.find_element(By.CSS_SELECTOR, 'div[class="swatch-opt-1556"] > div[class="swatch-attribute color"]  div[option-label="Blue"]')
        button.click()

    def display_blue_color_selected(self):
        """Проверяем что кнопка Blue выбрана/подсвечена на 1 карточке товара home page"""
        cart = self.driver.find_element(By.CSS_SELECTOR, 'div[class="swatch-opt-1556"] > div[class="swatch-attribute color"]')
        wait = WebDriverWait(self.driver,5)
        value = cart.get_attribute('option-selected')

        assert int(value) == 50

    def click_promo_picture(self):
        """Клик по промо картинке ведущей в коллекцию"""
        picture_link = self.driver.find_element(By.CSS_SELECTOR, 'img[src="https://magento.softwaretestingboard.com/pub/media/wysiwyg/home/home-main.jpg"]')
        picture_link.click()

    def display_new_url_for_expected_url(self, expected_url):

        # Ожидаем определенный URL
        # WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # URL содержит expected_url
        assert expected_url in self.driver.current_url

    def click_sign_in(self):
        """Клик по sign in"""
        # часть href и текст
        sign_in_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/customer/account/login") and normalize-space(text())="Sign In"]')
        sign_in_link.click()

    def click_create_an_account(self):
        """Клик по create an account"""
        # часть href и текст
        create_an_account_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/customer/account/create") and normalize-space(text())="Create an Account"]')
        create_an_account_link.click()

