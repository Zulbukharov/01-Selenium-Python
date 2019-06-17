from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/math.html")

task = browser.find_element_by_id(
    "input_value")
inp = browser.find_element_by_id(
    "answer")
inp.send_keys(calc(task.text))

checkbox = browser.find_element_by_id(
    "robotCheckbox")

checkbox.click()

radio = browser.find_element_by_id(
    "robotsRule")
radio.click()

button = browser.find_element_by_css_selector(
    "button.btn")
button.click()


# option_1 =
