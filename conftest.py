import time
import allure
import requests
import pytest

from pytest import fixture
from selenium import webdriver
from config import Config


@allure.step("Waiting for resource availability {url}")
def url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://mcdonalds.ru", help="choose your browser")
    parser.addoption("--env", action="store", default="prod", help="Environment to run tests against")
    parser.addoption("--executor", action="store", default='172.17.0.1', help="Remote selenium host")
    parser.addoption("--browser_version", action="store", help="Remote selenium host")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--video", action="store_true", default=True)


@fixture(scope='session')
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
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--browser_version")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")

    capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video
        }
    }

    driver = webdriver.Remote(
        command_executor=F"http://{executor}:4444/wd/hub",
        desired_capabilities=capabilities
    )

    driver.implicitly_wait(3)
    driver.maximize_window()

    def finalizer():
        video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"
        driver.quit()

        if request.node.status != 'passed':
            if video:
                allure.attach(
                    body=url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4)

        # Clear videos and logs from selenoid
        if video and url_data(video_url): requests.delete(url=video_url)

    request.addfinalizer(finalizer)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
