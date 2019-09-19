import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

example_languages = ['ru', 'fr', 'es']

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: for example, ru")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") 
    user_language = 'ru' if not (str(user_language) in example_languages) else user_language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()