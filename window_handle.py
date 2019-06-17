from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element_by_css_selector("button.trollface")
button.click()

print(browser.window_handles)

browser.switch_to.window(browser.window_handles[1])
# browser.switch_to.alert.accept()

task = browser.find_element_by_id(
    "input_value")
inp = browser.find_element_by_id(
    "answer")
inp.send_keys(calc(task.text))

button = browser.find_element_by_css_selector(
    "button.btn")
button.click()


# option_1 =
