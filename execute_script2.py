from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/execute_script.html")

task = browser.find_element_by_id(
    "input_value")
inp = browser.find_element_by_id(
    "answer")
inp.send_keys(calc(task.text))

browser.execute_script("window.scrollBy(0, 100);")

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
