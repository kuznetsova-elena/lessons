import allure
from pytest import fixture

from page_objects.BasePage import BasePage


@fixture
def page(browser):
    page = BasePage(browser)
    return page


@allure.step("Проскролить страницу вниз")
@fixture
def scroll_down_to_bottom(page, browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    yield
