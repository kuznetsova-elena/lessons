from page_objects.desktop.FooterPage import FooterPage


def test_all_titles_present(page):
    page.verify_element_on_page(FooterPage.ABOUT_US_TITLE)
    page.verify_element_on_page(FooterPage.CONTACTS_TITLE)
    page.verify_element_on_page(FooterPage.SUBSCRIBE_TITLE)
