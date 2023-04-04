import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru, en',
        help='Language'
    )

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    language = request.config.getoption('language')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    yield browser

    print("\nquit browser..")
    browser.quit()
