from selenium import webdriver
from selenium.webdriver.support.ui import Select


def sum(x, y):
    return str(int(x) + int(y))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/selects1.html")
select = Select(browser.find_element_by_tag_name("select"))

num1 = browser.find_element_by_id("num1")
num2 = browser.find_element_by_id("num2")
select.select_by_value(sum(num1.text, num2.text))
button = browser.find_element_by_css_selector("button.btn")
button.click()
# select.select_by_visible_text("Bar")
