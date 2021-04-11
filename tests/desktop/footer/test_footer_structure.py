from page_objects.desktop.FooterPage import FooterPage

from page_objects.BasePage import BasePage


def test_all_titles_present(browser):
    page = BasePage(browser)
    page.verify_element_on_page(FooterPage.ABOUT_US_TITLE)
    page.verify_element_on_page(FooterPage.CONTACTS_TITLE)
    page.verify_element_on_page(FooterPage.SUBSCRIBE_TITLE)


