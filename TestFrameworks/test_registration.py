from selenium import webdriver
import time
import datetime
import unittest


class TestRegistration1(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRegistration1, self).__init__(*args, **kwargs)
        self.links = ["http://suninjuly.github.io/registration1.html",
                      "http://suninjuly.github.io/registration2.html"]
        self.browser = webdriver.Chrome()
        self.welcome_text = ""

    def test_page_one(self):
        self.browser.get(self.links[0])
        print(self.links)
        self.fill_required()
        self.press_button()
        self.get_result_text()
        self.assertEqual(
            self.welcome_text, "Поздравляем! Вы успешно зарегистировались!", "wrong text")
        # time.sleep(4)

    def test_page_two(self):
        self.browser.get(self.links[1])
        self.fill_required()
        self.press_button()
        self.get_result_text()
        self.assertEqual(
            self.welcome_text, "", "wrong text")

    def get_result_text(self):
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = welcome_text_elt.text

    def press_button(self):
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

    def fill_required(self):
        elements = []
        elements.append(self.browser.find_element_by_css_selector(
            "div.first_block input.first"))
        elements.append(self.browser.find_element_by_css_selector(
            "div.first_block input.second"))
        elements.append(self.browser.find_element_by_css_selector(
            "div.first_block input.third"))
        for element in elements:
            element.send_keys("required")


if __name__ == '__main__':
    unittest.main()
