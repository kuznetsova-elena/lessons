from page_objects.MainPage import MainPage
from page_objects.locators import MainPageLocators, Footer


def test_is_title_about_us_present(browser):
    title = Footer.ABOUT_US_TITLE
    footer = MainPage(browser)
    footer.load(MainPageLocators.URL)
    footer.browser.find_element(*title)


def test_is_title_contacts_present(browser):
    title = Footer.CONTACTS_TITLE
    footer = MainPage(browser)
    footer.load(MainPageLocators.URL)
    footer.browser.find_element(*title)


def test_is_subscribe_title_present(browser):
    title = Footer.SUBSCRIBE_TITLE
    footer = MainPage(browser)
    footer.load(MainPageLocators.URL)
    footer.browser.find_element(*title)


