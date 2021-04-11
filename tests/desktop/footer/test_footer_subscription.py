import time
import pytest
import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from page_objects.desktop.FooterPage import FooterPage


def test_subscription_success_with_valid_email(browser, scroll_down_to_bottom, page):
    email = "test@mail.ru"

    page.find_element(FooterPage.EMAIL_FIELD).send_keys(email)
    page.find_element(FooterPage.UNCHECKED_CHECKBOX).click()
    page.find_element(FooterPage.SUBSCRIPTION_BUTTON).click()
    time.sleep(3)

    assert page.find_element(FooterPage.SUCCESS_SUBSCRIPTION_TITLE).text != "Подписывайтесь на рассылку"
    assert page.find_element(FooterPage.SUCCESS_SUBSCRIPTION_TITLE).text == "Вы успешно подписались!"
    assert page.find_element(FooterPage.SUBSCRIBE_MORE_BUTTON).text == "Ещё раз"


@pytest.mark.parametrize("email", ["test", "test@", "test@test", "test@test..ru", "test@.ru"])
def test_subscription_unsuccess_with_invalid_email(browser, scroll_down_to_bottom, page, email):
    page.find_element(FooterPage.EMAIL_FIELD).send_keys(email)
    page.find_element(FooterPage.UNCHECKED_CHECKBOX).click()
    page.find_element(FooterPage.SUBSCRIPTION_BUTTON).click()
    time.sleep(3)

    assert page.find_element(FooterPage.SUCCESS_SUBSCRIPTION_TITLE).text == "Подписывайтесь на рассылку"
    assert "Соглашаюсь на обработку персональных данных*" in browser.page_source
    assert page.cannot_find_element(FooterPage.SUBSCRIBE_MORE_BUTTON) == "NoSuchElementException"


def test_subscription_unsuccess_with_empty_email(browser, scroll_down_to_bottom, page):
    page.find_element(FooterPage.EMAIL_FIELD).send_keys("")
    page.find_element(FooterPage.UNCHECKED_CHECKBOX).click()
    page.find_element(FooterPage.SUBSCRIPTION_BUTTON).click()
    time.sleep(3)

    assert page.find_element(FooterPage.SUCCESS_SUBSCRIPTION_TITLE).text == "Подписывайтесь на рассылку"
    assert "Соглашаюсь на обработку персональных данных*" in browser.page_source
    assert page.cannot_find_element(FooterPage.SUBSCRIBE_MORE_BUTTON) == "NoSuchElementException"


def test_subscription_unsuccess_with_empty_checkbox(browser, scroll_down_to_bottom, page):
    email = "test@mail.ru"

    page.find_element(FooterPage.EMAIL_FIELD).send_keys(email)
    page.find_element(FooterPage.SUBSCRIPTION_BUTTON).click()
    time.sleep(3)

    assert page.find_element(FooterPage.SUCCESS_SUBSCRIPTION_TITLE).text == "Подписывайтесь на рассылку"
    assert "Соглашаюсь на обработку персональных данных*" in browser.page_source
    assert page.cannot_find_element(FooterPage.SUBSCRIBE_MORE_BUTTON) == "NoSuchElementException"
