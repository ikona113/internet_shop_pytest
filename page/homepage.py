from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/')

    def accept_agree(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button[class=' css-1n36tvh']")
        button.click()

    def click_argus(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'span img[src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/m/t/mt07-gray_main_1.jpg"]')
        element.click()

    def click_radiant_tee(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'span img[src="https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/s/ws12-orange_main_2.jpg"]')
        element.click()