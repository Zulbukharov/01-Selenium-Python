from selenium import webdriver
import time
import datetime


def fill_required():
    elements = []
    elements.append(browser.find_element_by_css_selector(
        "div.first_block input.first"))
    elements.append(browser.find_element_by_css_selector(
        "div.first_block input.second"))
    elements.append(browser.find_element_by_css_selector(
        "div.first_block input.third"))
    for element in elements:
        element.send_keys("required")


def fill_non_required():
    elements = []
    elements.append(browser.find_element_by_css_selector(
        "div.second_block input.first"))
    elements.append(browser.find_element_by_css_selector(
        "div.second_block input.second"))
    for element in elements:
        element.send_keys("non required")


def test1():
    fill_required()


def test2():
    fill_required()
    fill_non_required()


def test3():
    fill_non_required()


functions = [test1, test2, test3]
browser = webdriver.Chrome()
for i in range(len(functions)):
    print("[test][", i, "][", datetime.datetime.now(), "]")
    browser.get("http://suninjuly.github.io/registration2.html")
    functions[i]()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    if i == 2:
        assert "Поздравляем! Вы успешно зарегистировались!" != welcome_text
    if i != 2:
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
    print("[success][", i, "]")

browser.quit()
