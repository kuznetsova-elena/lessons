from page_objects.MainPage import MainPage
from page_objects.locators import Footer

class FooterPage(MainPage):

    def is_title_present(self, title):
        element = self.browser.find_element(title)
        return element
