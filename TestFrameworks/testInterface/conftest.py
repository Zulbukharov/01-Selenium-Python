from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb")


@pytest.fixture(scope="function")
def browser(request):
    languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        print("\nopening page")
        browser.get(
            "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language))
    else:
        print("\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb".format(language))
        pytest.fail("Wrong Language")
        # assert 0
    yield browser
    print("\nquit browser..")
    browser.quit()
