import pytest
from selenium import webdriver
# import time


def test_page_contains_basket(browser):
    # time.sleep(30)
    basket = browser.find_element_by_css_selector(
        "form button.btn-add-to-basket")
    print(basket.text)
