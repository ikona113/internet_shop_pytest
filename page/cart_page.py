import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_size_m(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'div[option-label="M"]')
        button.click()

    def click_color_gray(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'div[option-label="Gray"]')
        button.click()

    def click_add_to_cart(self):
        """Нажать кнопку -> Add to Cart"""
        element = self.driver.find_element(By.CSS_SELECTOR, "button[title='Add to Cart']")
        element.click()

    def display_cart_one_element(self):
        """Проверить что в корзине 1 товар"""
        cart = self.driver.find_element(By.XPATH, "//*[@class='action showcart']//span[contains(@class, 'counter ')]")
        wait = WebDriverWait(self.driver,5)
        wait.until_not(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, "//*[@class='action showcart']//span[contains(@class, 'counter ')]"),
                'class',
                '_block-content-loading'
            )
        )
        assert '1' in cart.text


