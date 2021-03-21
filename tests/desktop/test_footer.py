from page_objects.desktop.MainPage import MainPage
from page_objects.desktop.CartPage import CartPage
from page_objects.desktop.FooterPage import FooterPage


class FooterTests:
    def test_is_title_about_us_present(self, browser):
        title = FooterPage.ABOUT_US_TITLE
        footer = MainPage(browser)
        footer.browser.find_element(*title)

    def test_is_title_contacts_present(self, browser):
        browser.open(CartPage.URL)
        title = FooterPage.CONTACTS_TITLE
        footer = MainPage(browser)
        footer.browser.find_element(*title)

    def test_is_subscribe_title_present(self, browser):
        title = FooterPage.SUBSCRIBE_TITLE
        footer = MainPage(browser)
        footer.browser.find_element(*title)
