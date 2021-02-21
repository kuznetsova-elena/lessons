class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _click(self, locator: tuple):
        self.browser.find_element(*locator).click()
