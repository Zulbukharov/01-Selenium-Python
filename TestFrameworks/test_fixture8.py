import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope='function')
def browser():
    print("\n[start browser for test]")
    browser = webdriver.Chrome()
    yield browser
    print("[quited browser]")
    browser.quit()


class TestMainPage(object):
    @pytest.mark.smoke  # обязательно выполнить
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression  # перед deploy
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(
            ".basket-mini .btn-group > a")
