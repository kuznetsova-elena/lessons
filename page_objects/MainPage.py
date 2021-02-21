from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.locators import MainPageLocators


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self, element):
        self.browser.get(element)
        self.browser.maximize_window()

    def click_product(self, product):
        element = self.browser.find_element(*product)
        element.click()

    def add_to_cart(self):
        button = self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def open_cart(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.OPEN_CART_BUTTON)
        )
        # element.click()

    def is_element_present(self, element):
        return self.browser.find_element(element)
