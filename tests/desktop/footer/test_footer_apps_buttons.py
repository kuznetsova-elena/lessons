from page_objects.BasePage import BasePage
from page_objects.desktop.FooterPage import FooterPage

import pytest


def test_instagram_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.INSTAGRAM_ICON)
    assert browser.current_url == f"{page.INSTAGRAM}"


def test_facebook_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.FACEBOOK_ICON)
    assert browser.current_url == f"{page.FACEBOOK}"


def test_vk_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.VK_ICON)
    assert browser.current_url == f"{page.VK}"


def test_youtube_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.YOUTUBE_ICON)
    assert browser.current_url == f"{page.YOUTUBE}"


@pytest.mark.skip(reason='TODO')
def test_viber_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.VIBER_ICON)
    print(browser.current_url)
    assert browser.current_url == f"{page.VIBER}"


def test_whatsapp_button(browser, scroll_down_to_bottom, page):
    page.go_to_third_party_site(FooterPage.WHATSAPP_ICON)
    assert browser.current_url == f"{page.WHATSAPP}"






