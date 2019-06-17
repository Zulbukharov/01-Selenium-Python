from selenium import webdriver


def send_data(browser):
    first_name = browser.find_element_by_xpath("//input[@name='first_name']")
    first_name.send_keys("Abl")
    last_name = browser.find_element_by_xpath("//input[@name='last_name']")
    last_name.send_keys("Abl")
    city = browser.find_element_by_xpath("//input[@class='form-control city']")
    city.send_keys("Abl")
    country = browser.find_element_by_xpath("//input[@id='country']")
    country.send_keys("abl")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def main():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    send_data(browser)
