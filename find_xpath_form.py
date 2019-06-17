from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

elements = browser.find_elements_by_xpath("//input")
for element in elements:
    element.send_keys("yay")

button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()
