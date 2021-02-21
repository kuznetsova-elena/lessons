from pytest import fixture
from selenium import webdriver
from config import Config
from page_objects.MainPage import MainPage

#
# @fixture(scope='function')
# def close_browser(browser):
#     browser.close()
#     return browser


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://mcdonalds.ru", help="choose your browser")
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests against")


@fixture
def url(request):
    return request.config.getoption("--url")


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome()
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(3)
    driver.maximize_window()

    # request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
