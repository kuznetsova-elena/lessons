from page_objects.desktop.FooterPage import FooterPage


def test_appstore_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.APP_STORE_BUTTON)
    assert browser.current_url == f"{page.APP_STORE_URL}"


def test_google_play_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.GOOGLE_PLAY_BUTTON)
    assert browser.current_url == f"{page.GOOGLE_PLAY_URL}"


def test_app_gallery_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.APP_GALLERY_BUTTON)
    assert browser.current_url == f"{page.APP_GALLERY_URL}"
