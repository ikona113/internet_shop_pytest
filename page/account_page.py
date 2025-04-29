import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open_register(self):
        """Открываем страницу регистрации"""
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def open_authorization(self):
        """Открываем страницу авторизации"""
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/login/')

    def input_first_name(self, first_name):
        """Заполнить поле First Name текстом из переменной first_name"""
        find_input = self.driver.find_element(By.XPATH, '//input[@title="First Name"]')
        find_input.send_keys(first_name)

    def input_last_name(self, last_name):
        """Заполнить поле Last Name текстом из переменной last_name"""
        find_input = self.driver.find_element(By.XPATH, '//input[@title="Last Name"]')
        find_input.send_keys(last_name)


    def input_email(self, email):
        """Заполнить поле Email текстом из переменной email"""
        find_input = self.driver.find_element(By.XPATH, '//input[@title="Email"]')
        find_input.send_keys(email)

    def input_password(self, password):
        """Заполнить поле Password текстом из переменной password"""
        find_input = self.driver.find_element(By.XPATH, '//input[@title="Password"]')
        find_input.send_keys(password)

    def input_confirm_password(self, confirm_password):
        """Заполнить поле Confirm Password текстом из переменной confirm_password"""
        find_input = self.driver.find_element(By.XPATH, '//input[@title="Confirm Password"]')
        find_input.send_keys(confirm_password)

    def click_create_an_account(self):
        """Нажать кнопку Create an Account"""
        find_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="action submit primary"]'))
        )
        find_button.click()

    def display_new_url_for_registration(self):
        """Проверим что открылся профиль"""
        expected_url = 'https://magento.softwaretestingboard.com/customer/account/'
        assert WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))