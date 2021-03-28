from page_objects.desktop.FooterPage import FooterPage
from page_objects.desktop.MainPage import MainPage


def test_is_title_about_us_present(browser):
    main_page = MainPage(browser)
    # main_page.verify_element_on_page(FooterPage.ABOUT_US_TITLE)
    # main_page.verify_element_on_page(FooterPage.CONTACTS_TITLE)
    # main_page.verify_element_on_page(FooterPage.SUBSCRIBE_TITLE)
    main_page.click_product(FooterPage.ABOUT_US_TITLE)
