from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

elements = browser.find_elements_by_css_selector("input.form-control")
for element in elements:
    element.send_keys("hui")

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'registration.py')

file = browser.find_element_by_id("file")
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
