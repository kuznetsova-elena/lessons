from page_objects.desktop.MainPage import MainPage
from page_objects.desktop.CartPage import CartPage


def test_is_title_about_us_present(browser):
    title = Footer.ABOUT_US_TITLE
    footer = MainPage(browser)
    footer.browser.find_element(*title)


def test_is_title_contacts_present(browser):
    browser.open(CartPage.URL)
    title = Footer.CONTACTS_TITLE
    footer = MainPage(browser)
    footer.browser.find_element(*title)


def test_is_subscribe_title_present(browser):
    title = Footer.SUBSCRIBE_TITLE
    footer = MainPage(browser)
    footer.browser.find_element(*title)
