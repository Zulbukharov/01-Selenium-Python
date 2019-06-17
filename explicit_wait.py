from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
    # EC.element_to_be_clickable((By.ID, "price"))
    # selenium.webdriver.support.expected_conditions.title_is()
    # EC.text_to_be_present_in_element("s")
    # browser.find_element_by_id("price").title_is("1000")
    # EC.title_is("10000")
    EC.text_to_be_present_in_element((By.ID, "price"), "10000")
)
button = browser.find_element_by_id("book")
button.click()
# message = browser.find_element_by_id("check_message")

task = browser.find_element_by_id(
    "input_value")
inp = browser.find_element_by_id(
    "answer")
inp.send_keys(calc(task.text))

button = browser.find_element_by_id("solve")
button.click()

# assert "успешно" in message.text
