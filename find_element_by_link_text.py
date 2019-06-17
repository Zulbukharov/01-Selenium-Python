import math
from selenium import webdriver
import find_element

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"
browser.get(link)

number = browser.find_element_by_link_text(
    str(math.ceil(math.pow(math.pi, math.e)*10000)))
number.click()
find_element.send_data(browser)
