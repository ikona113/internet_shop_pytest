from page.homepage import HomePage
import pytest


def asd(driver):
    HomePage.open1(driver)
    HomePage.accept_agree()
    HomePage.click_argus()