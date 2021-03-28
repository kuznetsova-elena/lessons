import allure
import selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Выполняю клик по элементу {locator}")
    def _click(self, locator: tuple):
        self.verify_element_on_page(locator).click()

    @allure.step("Проверяю наличие элемента на странице")
    def verify_element_on_page(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator)).click()
        except selenium.common.exceptions.TimeoutException:
            self.browser.save_screenshot("exception.png")
            raise AssertionError("Элемент {} не найден на странице".format(locator))
