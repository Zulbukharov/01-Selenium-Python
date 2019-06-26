import pytest
from selenium import webdriver
import time
import math

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture
def browser():
    print("\n[starting browser]")
    browser = webdriver.Chrome()
    yield browser
    print("\n[quting browser]")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_send_correct_answer(browser, link):
    print(link)
    browser.get(link)
    browser.implicitly_wait(5)
    textarea = browser.find_element_by_css_selector(
        "textarea.textarea")
    answer = math.log(int(time.time()))
    print(answer)
    textarea.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    browser.implicitly_wait(5)
    text = browser.find_element_by_css_selector("pre.smart-hints__hint")
    print(text.text)
