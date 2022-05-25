import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as ffOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en',
                     help='Choose one of the languages: ar, ca, cs, da, de, en, en-gb, el, es, fi, fr, it, ko,pl, pt,'
                          'pt-br, ro, ru, sk, uk, zh-hans')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')

    scope_of_languages = ['ar', 'ca', 'cs', 'da', 'de', 'en', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'pl', 'pt',
                          'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']
    if language not in scope_of_languages:
        raise pytest.UsageError("--language should be one of the languages: ar, ca, cs, da, de, en-gb, el, es, fi, fr,"
                                "it, ko, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

    if browser_name == 'chrome':
        language_option = Options()
        language_option.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=language_option)
    elif browser_name == 'firefox':
        language_option = ffOptions()
        language_option.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=language_option)
    else:
        raise pytest.UsageError('--browser name should be chrome or firefox')

    yield browser

    browser.quit()
